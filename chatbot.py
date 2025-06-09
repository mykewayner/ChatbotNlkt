from bs4 import BeautifulSoup
import requests
from gpt4all import GPT4All
from pathlib import Path

# Caminho para o modelo local
modelo = Path("models/mistral-7b-instruct-v0.1.Q4_K_M.gguf").resolve()
llm = GPT4All(model_name=modelo.name, model_path=str(modelo.parent), allow_download=False)

def buscar_na_wiki(pergunta):
    termo = pergunta.replace(" ", "+")
    url_busca = f"https://terraria.wiki.gg/pt/index.php?search={termo}"
    resp = requests.get(url_busca, allow_redirects=True)
    soup = BeautifulSoup(resp.text, "html.parser")

    if "/wiki/" in resp.url and "search=" not in resp.url:
        print("Redirecionado para:", resp.url)
        soup_pg = soup
    else:
        link = soup.select_one("ul.mw-search-results li a")
        if not link:
            return "Não encontrei nada relevante na wiki para isso."

        href = link["href"]
        url_pagina = "https://terraria.wiki.gg" + href
        print("Acessando:", url_pagina)
        resp_pg = requests.get(url_pagina)
        soup_pg = BeautifulSoup(resp_pg.text, "html.parser")

    conteudo = soup_pg.select_one("#mw-content-text")
    texto = conteudo.get_text(separator="\n").strip() if conteudo else soup_pg.get_text()

    return texto[:4000]

def responder(pergunta):
    contexto = buscar_na_wiki(pergunta)
    if "Não encontrei nada" in contexto:
        return contexto

    prompt = (
        "Você é um assistente especialista no jogo Terraria. "
        "Sempre responda em português do Brasil, de forma clara e objetiva.\n\n"
        f"Baseado neste conteúdo da wiki:\n{contexto}\n\n"
        f"Usuário: {pergunta}\nBot:"
    )

    resposta = llm.generate(prompt=prompt)
    return resposta.strip()

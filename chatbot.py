import nltk
import random
from nltk.chat.util import Chat, reflections
from pairs import pairs;


reflections = {
    "eu sou": "você é",
    "eu": "você",
    "meu": "seu",
    "minha": "sua",
    "me": "te",
    "você é": "eu sou",
    "você": "eu",
    "seu": "meu",
    "sua": "minha"
}


chatbot = Chat(pairs, reflections)

def responder(mensagem):
    resposta = chatbot.respond(mensagem)

    # Se não entendeu nada, responde genérico
    if not resposta:
        return "Hmm... não entendi muito bem. Pode reformular?"

    # Lista de respostas que **não** devem gerar follow-up
    respostas_sem_follow_up = [
        "Olá, Pronto pra explorar o mundo de Terraria?",
        "Boa sorte nas suas aventuras! Que a Espada de Terra esteja com você."
    ]

    # Se for uma dessas, retorna direto
    if resposta in respostas_sem_follow_up:
        return resposta

    # Caso contrário, adiciona uma pergunta extra
    follow_ups = [
        "O que mais você gostaria de saber?",
        "Tem mais alguma dúvida?",
        "Quer falar sobre outro assunto?",
        "Posso te ajudar com mais alguma coisa?"
    ]

    return resposta + " " + random.choice(follow_ups)
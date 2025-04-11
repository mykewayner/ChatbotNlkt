import nltk
from nltk.chat.util import Chat, reflections

# Padrões de perguntas e respostas (você pode personalizar depois)
pairs = [
    [
        r"oi|olá|ei",
        ["Olá! Como posso te ajudar?"]
    ],
    [
        r"qual seu nome?",
        ["Sou um chatbot temático em Python."]
    ],
    [
        r"(.*) ajuda (.*)",
        ["Claro, estou aqui para ajudar. Me diga sua dúvida."]
    ],
    [
        r"sair",
        ["Tchau! Até a próxima."]
    ],
    [
        r"(.*)",
        ["Desculpe, não entendi. Pode repetir?"]
    ]
]

chatbot = Chat(pairs, reflections)

def responder(mensagem):
    return chatbot.respond(mensagem)

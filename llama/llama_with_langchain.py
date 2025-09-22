from langchain.schema import HumanMessage, SystemMessage
import requests
import json

def call_ollama_stream(messages, model="llama3"):
    url_ollama = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "stream": True,  # streaming ativo
        "messages": [
            {"role": "system" if isinstance(m, SystemMessage) else "user", "content": m.content}
            for m in messages
        ]
    }

    resposta_completa = ""  # para armazenar toda a resposta
    with requests.post(url_ollama, json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "message" in data and "content" in data["message"]:
                    token = data["message"]["content"]
                    print(token, end="", flush=True)  # imprime conforme chega
                    resposta_completa += token
    print()  # pula linha no final
    return resposta_completa  # retorna a resposta completa para salvar no histórico

# Configuração do bot do langchain
system_prompt = SystemMessage(content="""
Você é um assistente técnico especialista em LangChain, LLMs e Ollama.
Sempre responda de forma objetiva e didática.
""")

conversation_history = [system_prompt]

print("Chatbot iniciado! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        break

    conversation_history.append(HumanMessage(content=user_input))
    resposta = call_ollama_stream(conversation_history)
    conversation_history.append(SystemMessage(content=resposta))  # salva no histórico

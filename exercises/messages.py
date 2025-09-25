from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Config de ambiente
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROK_KEY")

def agent1():
    # Modelo LLM
        model = ChatGroq(
            model="llama-3.1-8b-instant",  # pode usar também mixtral-8x7b, gemma-7b, etc
            temperature=0
        ) 

        messages = [
            SystemMessage("Você é uma robô chamada Helena que gosta de livros, rpgs e cultura nerd.."),
        ]

        response = model.invoke(messages)
        print(response.content)

def agent2():
    # Modelo LLM
    model = ChatGroq(
        model="llama-3.1-8b-instant",  # pode usar também mixtral-8x7b, gemma-7b, etc
        temperature=0
    ) 

    messages = [
        SystemMessage("Você é um assistente Python."),
    ]

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break

        messages.append(HumanMessage(user_input))
        response = model.invoke(messages)
        messages.append(response)

        print(f"Assistente: {response.content}")
        
        
print("Escolha o agente que você quer usar:")

while True:
    choice = input("1 - Agente 1 (Haiku)\n2 - Agente 2 (Assistente Python)\nDigite 1 ou 2 (ou 'sair' para encerrar): ")
    if choice == "1":
        agent1()
    elif choice == "2":
        agent2()
    elif choice.lower() == "sair":
        break
    else:
        print("Escolha inválida. Tente novamente.")
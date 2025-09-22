import requests

url_ollama = 'http://localhost:11434/api/chat'

knowledge = """
Você é um assistente técnico especialista em LangChain, LLMs e Ollama.
Você deve responder de forma objetiva e didática.
Sempre use exemplos quando for útil.
"""

message_list = [{"role": "system", "content":knowledge }]

print("Chat iniciado! Digite 'sair' para encerrar \n")

while True:
  user_input = input("Você: ")
  if user_input.lower() in ["sair", "exit", "quit"]:
    break
  
  message_list.append([{"role": "user", "content": user_input}])
  
  res = requests.post(url_ollama, json={
    "model": "llama3",
    "stream": False,
    "messages": message_list
  })
  
  result = res.json()["message"]["content"]
  print("Bot: ", result)
  
  message_list.append({"role": "assistent", "content": result})
  
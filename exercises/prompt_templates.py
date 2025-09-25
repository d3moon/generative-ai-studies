from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from config import init_model

# Inicializar modelo
llm = init_model()

# Criar template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Qual a capital da {topic}?"),
])

# Gerar mensagens preenchidas
formatted_prompt = prompt_template.format(topic="Alemanha")

# Passar para o modelo
result = llm.invoke(formatted_prompt)

print(result.content)

prompt_template2 = ChatPromptTemplate([
    ("system", "Você é um assistente útil que responde perguntas com clareza."),
    MessagesPlaceholder("mensagens"),  # Aqui vai o histórico
    ("user", "Responda: {pergunta}")
])

historico = [
    HumanMessage(content="Qual é a capital da França?"),
    AIMessage(content="A capital da França é Paris."),
    HumanMessage(content="E a da Alemanha?")
]

# Gerar mensagens preenchidas
formatted_prompt = prompt_template2.format(mensagens=historico, pergunta="E a da Itália?")

resultado = llm.invoke({"mensagens": historico, "pergunta": "E a da Itália?"})
print(resultado.content)
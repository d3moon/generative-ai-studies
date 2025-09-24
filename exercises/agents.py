import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.tools import tool
from langchain.agents import create_agent, ToolNode
from langchain_groq import ChatGroq

# Config de ambiente
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROK_KEY")

# Modelo LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",  # pode usar também mixtral-8x7b, gemma-7b, etc
    temperature=0
) 

# Saída estruturada
class GuitarSetup(BaseModel):
    guitar: str

# Definição da tool
@tool
def guitar_recommendation(style: str) -> dict:
    """Recomenda guitarras para diferentes estilos de música."""
    style = style.lower()
    if "metal" in style:
        return {"guitar": "ESP LTD EC-1000 com EMG 81/85"}
    elif "blues" in style:
        return {"guitar": "Fender Stratocaster American Professional II"}
    elif "jazz" in style:
        return {"guitar": "Gibson ES-335"}
    else:
        return {"style": "Yamaha Pacifica — versátil pra iniciantes e intermediários"}

tool_node = ToolNode(
    tools=[guitar_recommendation],
    handle_tool_errors=lambda e: f"Erro tratado: {e}"
)
# Agent que consegue chamar a tool
agent = create_agent(
    llm,
    tools=[guitar_recommendation],
    prompt="Você é um especialista em guitarras, responda de forma direta e detalhada em uma linha."
    )

# Execução
result = agent.invoke({
    "messages": [{"role": "user", "content": "Preciso de uma guitarra boa para tocar blues."}]
})

print(result)
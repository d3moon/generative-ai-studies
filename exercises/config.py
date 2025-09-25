from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Configuração de ambiente

def init_model():
  load_dotenv()
  os.environ["GROQ_API_KEY"] = os.getenv("GROK_KEY")

  llm = ChatGroq(
      model="llama-3.1-8b-instant",
      temperature=0
  )
  
  return llm

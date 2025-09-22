import os
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_KEY")

# Jeito moderno de instanciar classes do Chat Model do Gemini -> https://docs.langchain.com/oss/python/integrations/providers/google#google-generative-ai-gemini-api-and-ai-studio
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# Jeito tradicional
# llm = init_chat_model(
#     "gemini-1.5-flash",
#     model_provider="google_genai",
#     temperature=0.7
# )

system_msg = SystemMessage("Você é um assistente feito para ajudar a escolher guitarras.")
human_msg = HumanMessage("Liste 3 guitarras para heavy metal e metal progressivo. Faça somente isso.")

messages = [system_msg, human_msg]

result = llm.invoke(messages)
print(result.content)

from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    return ChatOllama(
        model="mistral", 
        temperature=0.1,
        base_url="http://localhost:11434" 
    )
    
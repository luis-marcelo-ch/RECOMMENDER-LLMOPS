import os
from dotenv import load_dotenv

load_dotenv()   # load all environment variables

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
#MODEL_NAME = "llama-3.1-8b-instant"
MODEL_NAME = "openai/gpt-oss-20b"

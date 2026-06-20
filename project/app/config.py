from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_MODEL = "mistral-small-2506"

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY") 

print("MISTRAL_API_KEY:", MISTRAL_API_KEY)
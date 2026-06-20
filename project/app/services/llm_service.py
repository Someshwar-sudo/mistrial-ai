from langchain_mistralai import ChatMistralAI
from app.config import MISTRAL_MODEL, MISTRAL_API_KEY


class LLMService:

    @staticmethod
    def load_model():

        return ChatMistralAI(
            model_name=MISTRAL_MODEL,
            api_key=MISTRAL_API_KEY   
        )
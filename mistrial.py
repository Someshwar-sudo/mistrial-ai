# import the packages

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

#load the dotenv
load_dotenv()

Model = ChatMistralAI(model='mistral-small-2506',temperature=0.9,max_tokens=20)

response = Model.invoke('Tell me the kids poem').content

print(response)
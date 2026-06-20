from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from typing import List,Optional

load_dotenv()

model = ChatMistralAI(model_name='mistral-small-2506',)

class Movie(BaseModel):
    title : str
    release_year : Optional[int]
    director : str
    genre : List[str]
    rating :Optional[float]
    summary :str
    
parser = PydanticOutputParser(pydantic_object = Movie)

prompt = ChatPromptTemplate.from_messages([
        ('system',"""
            Extract movie information from the paragraph
            {format_instructions}
        """),
        ("human","{paragraph}")
        ]
        )
para = input('Give your paragraph : ')

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions()
     }
)

response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)

print(movie_data)
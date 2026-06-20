from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()


model = ChatMistralAI(model_name="mistral-small-2506")


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    director: str
    genre: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Extract movie information from the paragraph.\n{format_instructions}"
    ),
    ("human", "{paragraph}")
])


class MovieExtractor:

    def __init__(self):
        self.model = model
        self.prompt = prompt
        self.parser = parser

    def extract(self, paragraph: str):
        final_prompt = self.prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": self.parser.get_format_instructions()
        })

        response = self.model.invoke(final_prompt)
        movie_data = self.parser.parse(response.content)

        return movie_data.model_dump()
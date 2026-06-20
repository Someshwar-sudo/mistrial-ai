import gradio as gr
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

# ---------------- MODEL ----------------
model = ChatMistralAI(model_name="mistral-small-2506")

# ---------------- SCHEMA ----------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    director: str
    genre: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
     Extract movie information from the paragraph.
     Return strictly in the required format.
     {format_instructions}
     """
    ),
    ("human", "{paragraph}")
])

# ---------------- CORE FUNCTION ----------------
def extract_movie_info(paragraph: str):
    try:
        final_prompt = prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })

        response = model.invoke(final_prompt)
        movie_data = parser.parse(response.content)

        return movie_data.dict()

    except Exception as e:
        return {"error": str(e)}

# ---------------- GRADIO UI ----------------
interface = gr.Interface(
    fn=extract_movie_info,
    inputs=gr.Textbox(lines=10, placeholder="Paste movie paragraph here..."),
    outputs=gr.JSON(),
    title="🎬 Movie Intelligence LLM",
    description="Extract structured movie data (title, director, genre, rating, summary) from raw text using LLM."
)

if __name__ == "__main__":
    interface.launch()
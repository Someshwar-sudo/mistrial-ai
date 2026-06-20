from langchain_core.output_parsers import PydanticOutputParser

from app.schemas.movie_schema import Movie


class ParserService:

    @staticmethod
    def get_parser():

        return PydanticOutputParser(

            pydantic_object=Movie

        )
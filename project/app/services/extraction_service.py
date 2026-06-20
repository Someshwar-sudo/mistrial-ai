from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from app.services.parser_service import ParserService


class ExtractionService:

    def __init__(self):

        self.llm = LLMService.load_model()

        self.prompt = PromptService.movie_prompt()

        self.parser = ParserService.get_parser()

    def extract(self, paragraph):

        final_prompt = self.prompt.invoke(

            {

                "paragraph": paragraph,

                "format_instructions":

                self.parser.get_format_instructions()

            }

        )

        response = self.llm.invoke(final_prompt)

        return self.parser.parse(

            response.content

        )
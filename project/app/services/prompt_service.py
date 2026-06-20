from langchain_core.prompts import ChatPromptTemplate


class PromptService:

    @staticmethod
    def movie_prompt():

        return ChatPromptTemplate.from_messages(

            [

                (

                    "system",

                    """
                    You are an expert Movie Information Extraction assistant.

                    Extract the movie information from the given paragraph.

                    {format_instructions}
                    """

                ),

                (

                    "human",

                    "{paragraph}"

                )

            ]

        )
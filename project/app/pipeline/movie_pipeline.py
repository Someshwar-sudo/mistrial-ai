from app.services.extraction_service import ExtractionService


class MoviePipeline:

    def __init__(self):
        self.extractor = ExtractionService()

    def run(self, paragraph):

        movie = self.extractor.extract(paragraph)

        # 🔴 Safety check
        if movie is None:
            return {"error": "Extractor returned None"}

        # If it's already a dict
        if isinstance(movie, dict):
            return movie

        # If it's a Pydantic model
        if hasattr(movie, "model_dump"):
            return movie.model_dump()

        # fallback (LLM returned string or unknown type)
        return {"result": str(movie)}
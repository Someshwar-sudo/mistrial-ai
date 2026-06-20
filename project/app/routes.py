from fastapi import APIRouter
from pydantic import BaseModel
from app.pipeline.movie_pipeline import MoviePipeline

router = APIRouter()
pipeline = MoviePipeline()


class MovieRequest(BaseModel):
    text: str


@router.post("/extract")
def extract_movie(payload: MovieRequest):
    try:
        result = pipeline.run(payload.text)

        # Ensure JSON-safe response
        return {"result": result}

    except Exception as e:
        return {"error": str(e)}
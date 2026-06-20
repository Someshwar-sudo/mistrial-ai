from pydantic import BaseModel
from typing import List, Optional


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    director: str
    genre: List[str]
    rating: Optional[float]
    summary: str
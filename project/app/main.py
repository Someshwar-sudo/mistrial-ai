from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Movie Intelligence API"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Movie Intelligence API is Running "
    }
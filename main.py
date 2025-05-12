from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Greetrequest(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in Docker!"}


# from fastapi import FastAPI
# from .routes import router

# app = FastAPI(title="Fibonacci API")

# app.include_router(router)

# @app.post("/generate")
# def home():
#     return {"message": "Welcome to Fibonacci Generator API"}

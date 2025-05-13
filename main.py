from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Greetrequest(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in Docker!"}

# check2
@app.post("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

























# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Greetrequest(BaseModel):
#     name: str


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI example!"}

# @app.post("/greet/{name}")
# def greet_user(name: str):
#     return {"message": f"Hello, {name}!"}



from fastapi.testclient import TestClient
from main import app
import httpx

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI in Docker!"}

def test_greet_user():
    response = client.post("/greet/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}





# from fastapi.testclient import TestClient
# from main import app
# import httpx

# client = TestClient(app)

# def test_get_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Welcome to the FastAPI example!"}
# def test_greet_user():
#     response = client.post("/greet/John")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello, John!"}    
from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    print('test_read_main')
    response = client.get("/users")
    print(response)
    assert response.status_code == 200

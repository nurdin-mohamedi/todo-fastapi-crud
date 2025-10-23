from fastapi.testclient import TestClient

from main import app
from utility import get_db, override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_server_working():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_get_all_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [
        {
            "title": "Create a CRUD application",
            "description": "Create a FastAPI CRUD application for managing todos",
            "is_complete": False,
        }
    ]

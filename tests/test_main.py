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


def test_get_todos_non_found():
    # TODO: Delete all todos
    response = client.get("/todos")
    assert response.status_code == 200
    # TODO: assert response.json() == {"message": "Todo not found"}


def test_get_todo_exist():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Create a CRUD application",
        "description": "Create a FastAPI CRUD application for managing todos",
        "is_complete": False,
    }


def test_get_todo_not_exist():
    response = client.get("/todos/10")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo not found"}

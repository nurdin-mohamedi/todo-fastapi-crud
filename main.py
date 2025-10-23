from typing import Any

from fastapi import FastAPI

app = FastAPI()


todos = [
    {
        "title": "Create a CRUD application",
        "description": "Create a FastAPI CRUD application for managing todos",
        "is_complete": False,
    }
]


@app.get("/")
def get_home() -> dict:
    return {"message": "Hello, World!"}


@app.get("/todos")
def get_todos() -> list[dict[str, Any]]:
    return todos

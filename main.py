from typing import Any

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from models import TodoBase
from schema import Todo
from utility import get_db

app = FastAPI()


@app.get("/")
def get_home() -> dict:
    return {"message": "Hello, World!"}


@app.get("/todos", response_model=list[TodoBase])
def get_todos(
    db: Session = Depends(get_db),
) -> Any:
    todos: list[Todo] = db.query(Todo).all()
    if todos:
        print(todos[0].title)
        print(todos[0].description)
        return todos
    return {"message": "Todos not found"}

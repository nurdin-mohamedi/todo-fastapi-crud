from typing import Annotated, Any

from fastapi import Depends, FastAPI, Path, Query
from sqlalchemy.orm import Session

from models import TodoBase
from schema import Todo
from utility import get_db

app = FastAPI()


@app.get("/")
def get_home() -> dict:
    return {"message": "Hello, World!"}


@app.get("/todos", response_model=list[TodoBase] | dict[str, str])
def get_todos(
    limit: Annotated[int | None, Query(ge=0, le=10)] = 10,
    offset: Annotated[int | None, Query(ge=0, le=10)] = 0,
    db: Session = Depends(get_db),
) -> Any:
    todos: list[Todo] = (
        db.query(Todo).offset(offset).limit(limit).all()
    )
    if todos:
        print(todos[0].title)
        print(todos[0].description)
        return todos
    return {"message": "Todos not found"}


@app.get("/todos/{todo_id}", response_model=TodoBase | dict[str, str])
def get_todo(
    todo_id: Annotated[int, Path(ge=1)], db: Session = Depends(get_db)
):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        return todo
    return {"message": "Todo not found"}

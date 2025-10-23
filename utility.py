from database import session
from schema import Base, Todo
from tests.conftest import session as test_session
from tests.conftest import test_engine


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def override_get_db():
    Base.metadata.create_all(test_engine)

    db = test_session()

    todos = [
        {
            "title": "Create a CRUD application",
            "description": "Create a FastAPI CRUD application for managing todos",
            "is_complete": False,
        }
    ]
    for todo in todos:
        db.add(Todo(**todo))
    print("Populating initial data")
    db.commit()

    try:
        yield db
    finally:
        db.close()

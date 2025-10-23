from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer(), primary_key=True, index=True)
    title = Column(String(100), unique=True)
    description = Column(String(200))
    is_complete = Column(Boolean())

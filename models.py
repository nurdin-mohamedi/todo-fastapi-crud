from pydantic import BaseModel, ConfigDict


class TodoBase(BaseModel):
    title: str
    description: str
    is_complete: bool

    model_config = ConfigDict(from_attributes=True)


class TodoModel(TodoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

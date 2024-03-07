from pydantic import BaseModel, Field


class TaskWithoutID(BaseModel):
    title: str = Field(max_length=255)
    description: str = Field(default=None, max_length=1000)
    done: bool = Field(default=False)


class Task(TaskWithoutID):
    id: int


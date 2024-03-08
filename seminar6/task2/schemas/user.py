from pydantic import BaseModel, Field, EmailStr


class UserWithoutID(BaseModel):
    name: str = Field(min_length=2, max_length=64)
    surname: str = Field(min_length=2, max_length=64)
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=8, max_length=32)


class User(UserWithoutID):
    id: int

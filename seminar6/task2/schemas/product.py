from pydantic import BaseModel, Field


class ProductWithoutID(BaseModel):
    title: str = Field(min_length=3, max_length=64)
    description: str = Field(max_length=256)
    price: int = Field(gt=0)


class Product(ProductWithoutID):
    id: int

from pydantic import BaseModel, Field
from datetime import date


class OrderWithoutID(BaseModel):
    id_user: int
    id_product: int
    order_date: date = Field()
    order_status: str = Field(max_length=16)


class Order(OrderWithoutID):
    id: int

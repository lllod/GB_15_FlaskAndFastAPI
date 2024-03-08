from schemas.order import Order, OrderWithoutID
from models import orders as order_model
from database.database import database
from typing import List
from fastapi import APIRouter
from faker import Faker
from datetime import datetime

router = APIRouter()
orders = order_model.orders
fake = Faker('ru_RU')


@router.get("/fake_orders/{count}")
async def create_fake_orders(count: int):
    for i in range(count):
        id_user = fake.random_int(min=1, max=20)
        id_product = fake.random_int(min=1, max=34)
        order_date = datetime.strptime(fake.date(), '%Y-%m-%d')
        order_status = fake.random_choices(elements=('Принят', 'В работе', 'Не оплачен', 'Выполнен'), length=1)[0]
        query = orders.insert().values(id_user=id_user, id_product=id_product, order_date=order_date,
                                       order_status=order_status)
        await database.execute(query)
    return {'message': f'{count} orders were created.'}


@router.get('/orders/', response_model=List[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get('/orders/{order_id}', response_model=Order)
async def get_order_by_id(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.post('/orders/', response_model=OrderWithoutID)
async def create_order(order: OrderWithoutID):
    query = orders.insert().values(**order.dict())
    await database.execute(query)
    return {**order.dict()}


@router.put('/orders/{order_id}', response_model=OrderWithoutID)
async def update_order(order_id: int, order: OrderWithoutID):
    query = orders.update().where(orders.c.id == order_id).values(**order.dict())
    await database.execute(query)
    return {**order.dict()}


@router.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': f'User id={order_id} deleted'}

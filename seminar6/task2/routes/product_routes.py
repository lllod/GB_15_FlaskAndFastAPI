from schemas.product import Product, ProductWithoutID
from models import products as product_model
from database.database import database
from typing import List
from fastapi import APIRouter
from faker import Faker

router = APIRouter()
products = product_model.products
fake = Faker('ru_RU')


@router.get("/fake_products/{count}")
async def create_fake_products(count: int):
    for i in range(count):
        title = fake.text(max_nb_chars=64)
        description = fake.text(max_nb_chars=256)
        price = fake.random_int(min=1)
        query = products.insert().values(title=title, description=description, price=price)
        await database.execute(query)
    return {'message': f'{count} products were created.'}


@router.get('/products/', response_model=List[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get('/products/{product_id}', response_model=Product)
async def get_product_by_id(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.post('/products/', response_model=ProductWithoutID)
async def create_product(product: ProductWithoutID):
    query = products.insert().values(**product.dict())
    await database.execute(query)
    return {**product.dict()}


@router.put('/products/{product_id}', response_model=ProductWithoutID)
async def update_product(product_id: int, product: ProductWithoutID):
    query = products.update().where(products.c.id == product_id).values(**product.dict())
    await database.execute(query)
    return {**product.dict()}


@router.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': f'User id={product_id} deleted'}

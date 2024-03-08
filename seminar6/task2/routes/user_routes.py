from schemas.user import User, UserWithoutID
from models import users as user_model
from database.database import database
from typing import List
from fastapi import APIRouter
from faker import Faker

router = APIRouter()
users = user_model.users
fake = Faker('ru_RU')


@router.get("/fake_users/{count}")
async def create_fake_tasks(count: int):
    for i in range(count):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.unique.email()
        password = fake.password(length=8)
        query = users.insert().values(name=name, surname=surname, email=email, password=password)
        await database.execute(query)
    return {'message': f'{count} users were created.'}


@router.get('/users/', response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get('/users/{user_id}', response_model=User)
async def get_user_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.post('/users/', response_model=UserWithoutID)
async def create_user(user: UserWithoutID):
    query = users.insert().values(**user.dict())
    await database.execute(query)
    return {**user.dict()}


@router.put('/users/{user_id}', response_model=UserWithoutID)
async def update_user(userd_id: int, user: UserWithoutID):
    query = users.update().where(users.c.id == userd_id).values(**user.dict())
    await database.execute(query)
    return {**user.dict()}


@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User id={user_id} deleted'}

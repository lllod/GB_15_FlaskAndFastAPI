# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из списка.


from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


app = FastAPI()
users = [User(id=i, name=f'Name_{i}', email=f'Email_{i}', password=f'Passwd_{i}') for i in range(1, 11)]


@app.get("/users/")
async def get_all_users():
    return users


@app.post('/add-user/')
async def add_user(user: User):
    users.append(user)
    return user


@app.put('/update-user/')
async def update_user(user_id: int, user: User):
    for i, looking_for_user in enumerate(users):
        if looking_for_user.id == user_id:
            users[i] = user
            return user
    return {'message': 'User not found'}


@app.delete('/delete-user/')
async def delete_user(user_id: int):
    for looking_for_user in users:
        if looking_for_user.id == user_id:
            users.remove(looking_for_user)
            return {'message': 'Removed complete'}
    return {'message': 'User not found'}

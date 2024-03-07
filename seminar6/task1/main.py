# Задание №4
# Напишите API для управления списком задач. Для этого создайте модель Task со следующими полями:
# id: int (первичный ключ)
# title: str (название задачи)
# description: str (описание задачи)
# done: bool (статус выполнения задачи)
# Задание №4 (продолжение)
# API должно поддерживать следующие операции:
# Получение списка всех задач: GET /tasks/
# Получение информации о конкретной задаче: GET /tasks/{task_id}/
# Создание новой задачи: POST /tasks/
# Обновление информации о задаче: PUT /tasks/{task_id}/
# Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.
import uvicorn
from fastapi import FastAPI
from models import Task, TaskWithoutID
import databases
import sqlalchemy
from typing import List
from faker import Faker

app = FastAPI()
fake = Faker('ru_RU')

DATABASE_URL = "sqlite:///seminar6task1.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table('tasks', metadata,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('title', sqlalchemy.String(255)),
                         sqlalchemy.Column('description', sqlalchemy.String(1000)),
                         sqlalchemy.Column('done', sqlalchemy.Boolean)
                         )

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


@app.on_event('startup')
async def connect_tables():
    await database.connect()


@app.on_event('shutdown')
async def close_tables():
    await database.disconnect()


@app.get("/fake_tasks/{count}")
async def create_fake_tasks(count: int):
    for i in range(count):
        title = fake.sentence(nb_words=5)
        description = fake.text(max_nb_chars=1000)
        done = fake.pybool()
        query = tasks.insert().values(title=title, description=description, done=done)
        await database.execute(query)
    return {'message': f'{count} tasks were created.'}


@app.get('/tasks/', response_model=List[Task])
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get('/tasks/{task_id}', response_model=Task)
async def get_task_by_id(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post('/tasks/', response_model=TaskWithoutID)
async def create_task(task: TaskWithoutID):
    query = tasks.insert().values(**task.dict())
    await database.execute(query)
    return {**task.dict()}


@app.put('/tasks/{task_id}', response_model=TaskWithoutID)
async def update_task(task_id: int, task: TaskWithoutID):
    query = tasks.update().where(tasks.c.id == task_id).values(**task.dict())
    await database.execute(query)
    return {**task.dict()}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': f'Task id={task_id} was deleted'}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000)

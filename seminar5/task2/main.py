# Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja
# для динамического формирования HTML страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы,
# таблицу со списком пользователей и кнопку для добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = [User(id=i, name=f'Name_{i}', email=f'Email_{i}', password=f'Passwd_{i}') for i in range(1, 11)]


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'name': 'ИИИИИИгорь'})


@app.get('/users/', response_class=HTMLResponse)
async def get_all_users(request: Request):
    return templates.TemplateResponse('users.html',
                                      {'request': request, 'title': 'All users table', 'users': users})


@app.post('/add-user/', response_class=HTMLResponse)
async def add_user(requsest: Request):
    return templates.TemplateResponse('add-user.html', {'request': requsest, 'title': 'Add new user'})

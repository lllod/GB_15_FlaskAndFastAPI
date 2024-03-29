# Задание №6
# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трех таблиц: товары, заказы и
# пользователи. Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных пользователях магазина. Таблица заказы должна содержать
# информацию о заказах, сделанных пользователями.
# Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),имя,фамилия, адрес электронной почты и пароль.
# Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
# Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
# id товара (FOREIGN KEY), дата заказа и статус заказа.
# Задание №6 (продолжение)
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление

from fastapi import FastAPI
from routes.event_routes import router as event_routes
from routes.user_routes import router as user_routes
from routes.product_routes import router as product_routes
from routes.order_routes import router as order_routes

app = FastAPI()

app.include_router(event_routes)
app.include_router(user_routes)
app.include_router(product_routes)
app.include_router(order_routes)

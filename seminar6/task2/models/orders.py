from sqlalchemy import MetaData, Integer, String, DATE, create_engine, Table, Column, ForeignKey
from database.database import DATABASE_URL
from models.users import users
from models.products import products

metadata = MetaData()

orders = Table('orders', metadata,
               Column('id', Integer, primary_key=True),
               Column('id_user', Integer, ForeignKey(users.c.id)),
               Column('id_product', Integer, ForeignKey(products.c.id)),
               Column('order_date', DATE()),
               Column('order_status', String(16))
               )

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

from sqlalchemy import MetaData, Integer, String, create_engine, Table, Column
from database.database import DATABASE_URL

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(64)),
              Column('surname', String(64)),
              Column('email', String(128)),
              Column('password', String(32))
              )

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

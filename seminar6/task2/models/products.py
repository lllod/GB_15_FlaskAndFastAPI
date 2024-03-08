from sqlalchemy import MetaData, Integer, String, create_engine, Table, Column
from database.database import DATABASE_URL

metadata = MetaData()

products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('title', String(64)),
                 Column('description', String(256)),
                 Column('price', Integer)
                 )

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

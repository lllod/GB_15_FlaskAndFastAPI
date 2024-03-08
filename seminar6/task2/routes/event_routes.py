from database import database as db
from fastapi import APIRouter

router = APIRouter()
database = db.database


@router.on_event('startup')
async def connect_tables():
    await database.connect()


@router.on_event('shutdown')
async def close_tables():
    await database.disconnect()

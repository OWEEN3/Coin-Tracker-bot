from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings

async_engine = create_async_engine(settings.DATABASE_URL)
session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
import asyncio

from sqlalchemy import select, insert, delete, and_

from database.models import Traking
from database.database import session_maker

class TrackingDAO:
    model = Traking
    
    @classmethod
    async def get_user_tracking(cls, chat_id: int):
        async with session_maker() as session:
            query = select(cls.model).where(
                cls.model.user_chat_id==chat_id
            )
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def add(cls, chat_id: int, symbol: str):
        async with session_maker() as session:
            query = insert(cls.model).values({
                cls.model.user_chat_id: chat_id,
                cls.model.symbol: symbol
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
    
    @classmethod
    async def delete(cls, chat_id: int, symbol: str):
        async with session_maker() as session:
            query = delete(cls.model).where(
                and_(cls.model.user_chat_id==chat_id, cls.model.symbol==symbol
                )
            )
            result = await session.execute(query)
            await session.commit()
            return True
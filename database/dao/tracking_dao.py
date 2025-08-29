from sqlalchemy import select, insert, delete

from database.models import Tracking
from database.database import session_maker

class TrackingDAO:
    model = Tracking
    
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
    async def delete(cls, id: int):
        async with session_maker() as session:
            query = delete(cls.model).where(cls.model.id==id)
            result = await session.execute(query)
            await session.commit()
            return True
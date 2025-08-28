from sqlalchemy import select, insert, update

from database.models import Users
from database.database import session_maker

class UsersDAO:
    model = Users
    
    @classmethod
    async def get_user(cls, chat_id: int):
        async with session_maker() as session:
            query = select(cls.model).where(
                cls.model.chat_id==chat_id
            )
            result = await session.execute(query)
            return result.scalars().one_or_none()
    
    @classmethod
    async def add_user(
        cls, 
        chat_id: int, 
        notification_type: str = "new", 
        notification_interval: int = 300
    ):
        async with session_maker() as session:
            query = insert(cls.model).values({
                cls.model.chat_id: chat_id,
                cls.model.notification_type: notification_type,
                cls.model.notification_interval: notification_interval
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
        
    @classmethod
    async def edit_notification_type(cls, notification_type: str):
        async with session_maker() as session:
            query = update(cls.model).values({
                cls.model.notification_type: notification_type
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
    
    @classmethod
    async def edit_notification_interval(
        cls, notification_interval: int
    ):
        async with session_maker() as session:
            query = update(cls.model).values({
                cls.model.notification_interval: notification_interval
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
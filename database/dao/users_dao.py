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
        notification_status: str = "off",
        notification_type: str = "new_message",
        notification_interval: int = 300
    ):
        async with session_maker() as session:
            query = insert(cls.model).values({
                cls.model.chat_id: chat_id,
                cls.model.notification_status: notification_status,
                cls.model.notification_type: notification_type,
                cls.model.notification_interval: notification_interval
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
        
    @classmethod
    async def edit_notification_type(
        cls, 
        chat_id: int,
        notification_type: str
    ):
        async with session_maker() as session:
            query = update(cls.model).where(
                cls.model.chat_id==chat_id
                ).values({
                cls.model.notification_type: notification_type
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
    
    @classmethod
    async def edit_notification_interval(
        cls, 
        chat_id: int,
        notification_interval: int
    ):
        async with session_maker() as session:
            query = update(cls.model).where(
                cls.model.chat_id==chat_id
            ).values({
                cls.model.notification_interval: notification_interval
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
    
    @classmethod
    async def edit_notification_status(
        cls,
        chat_id: int,
        notification_status: str
    ):
        async with session_maker() as session:
            query = update(cls.model).where(
                cls.model.chat_id==chat_id
            ).values({
                cls.model.notification_status: notification_status
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
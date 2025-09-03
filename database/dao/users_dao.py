from sqlalchemy import select, insert, update

from database.models import Users
from database.database import session_maker

class UsersDAO:
    model = Users
    
    @classmethod
    async def get_users(cls):
        async with session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
    
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
        update_status: str = "off",
        update_type: str = "update_message",
        update_interval: int = 300
    ):
        async with session_maker() as session:
            query = insert(cls.model).values({
                cls.model.chat_id: chat_id,
                cls.model.update_status: update_status,
                cls.model.update_type: update_type,
                cls.model.update_interval: update_interval
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
        
    @classmethod
    async def edit_update_type(
        cls, 
        chat_id: int,
        update_type: str
    ):
        async with session_maker() as session:
            query = update(cls.model).where(
                cls.model.chat_id==chat_id
                ).values({
                cls.model.update_type: update_type
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
    
    @classmethod
    async def edit_update_interval(
        cls, 
        chat_id: int,
        update_interval: int
    ):
        async with session_maker() as session:
            query = update(cls.model).where(
                cls.model.chat_id==chat_id
            ).values({
                cls.model.update_interval: update_interval
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
    
    @classmethod
    async def edit_update_status(
        cls,
        chat_id: int,
        update_status: str
    ):
        async with session_maker() as session:
            query = update(cls.model).where(
                cls.model.chat_id==chat_id
            ).values({
                cls.model.update_status: update_status
            }).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
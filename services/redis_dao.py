# import json
# import asyncio
from redis.asyncio import Redis
from services.redis_connection import redis_session

class RedisDAO:
    @classmethod
    @redis_session
    async def set(cls, r: Redis, key, value):
        await r.set(key, value)
        
    @classmethod
    @redis_session
    async def get(cls, r: Redis, key):
        return await r.get(key)
    
    @classmethod
    @redis_session
    async def delete(cls, r: Redis, key):
        await r.delete(key)
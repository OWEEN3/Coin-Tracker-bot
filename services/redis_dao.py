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

# async def main():
#     await RedisDAO.set(key="445408374", value=json.dumps(["BTCUSDT", "ETHUSDT"]))
#     value = json.loads(await RedisDAO.get(key="445408374"))
#     print(value)
#     await RedisDAO.delete(key="a")
#     value = await RedisDAO.get(key="a")
#     print(value)

# asyncio.run(main())
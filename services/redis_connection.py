from redis.asyncio import Redis
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import settings

def redis_session(func):
    async def wrapper(cls, *args, **kwargs):
        r = None
        try:
            r = Redis.from_url(url=await settings.REDIS_URL(), decode_responses=True)
            if await r.ping():
                result = await func(cls, r, *args, **kwargs)
                return result
            else:
                print("⚠️ Redis не отвечает")
        except Exception as e:
            print(f"❌ Ошибка подключения к Redis: {e}")
        finally:
            if r is not None:
                await r.aclose()
    return wrapper
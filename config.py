from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str
    
    model_config = SettingsConfigDict(
        env_file=ENV_PATH, env_file_encoding="utf-8"
    )
    
    @property
    def TOKEN(self):
        return self.BOT_TOKEN
    
    @property
    def DATABASE_URL_ALEMBIC(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    async def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

settings = Settings()
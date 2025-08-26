from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    TOKEN: str
    model_config = SettingsConfigDict(
        env_file=ENV_PATH, env_file_encoding="utf-8"
    )
    
    @property
    def get_token(self):
        return self.TOKEN

settings = Settings()
from attr import dataclass
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    tg_token: str
    api_key: str

    class Config:
        env_file=".env"
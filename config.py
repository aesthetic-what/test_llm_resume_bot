from attr import dataclass
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    tg_token: str

    class Config:
        env_file=".env"
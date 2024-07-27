import os
from dotenv import load_dotenv

load_dotenv()


class DB_CONFIG:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    @classmethod
    def get_db_url(cls, async_suff=False):
        return f"postgresql{'+asyncpg' * async_suff}://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"


class Config:
    POSTGRES = DB_CONFIG


cfg = Config()

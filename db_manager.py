from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from config import cfg
from models import *
# Async Engine

class DBManager:
    def __init__(self):
        engine = create_async_engine(cfg.POSTGRES.get_db_url(), echo=True)

        # Base class for our models
        Base = declarative_base()

# Async Session
        async_session = sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False
        )
        metadata = MetaData()
        res = metadata.create_all(async_session)
        print(res)


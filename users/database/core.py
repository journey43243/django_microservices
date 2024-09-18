from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine,text,engine
from .config import settings
from sqlalchemy import MetaData

engine_pg = engine.create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo = True,
    pool_size = 5,
    max_overflow = 15,
    
)


session_var = sessionmaker(engine_pg)

metadata = MetaData()


def create_tables():
    metadata.create_all(engine_pg)
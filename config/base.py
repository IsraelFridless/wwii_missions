from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql://postgres:1234@localhost/wwii_missions')
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    if not database_exists(engine.url):
        create_database(engine.url)
    return _SessionFactory()



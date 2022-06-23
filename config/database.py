import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

HOST = os.environ.get('POSTGRES_HOST', 'db')
USER = os.environ.get('POSTGRES_USER', 'db_user')
PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'db_pwd')
DB_NAME = os.environ.get('POSTGRES_DB', 'db_name')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal: Session.__class__ = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

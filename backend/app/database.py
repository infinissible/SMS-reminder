from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declaractive_base

DATABASE_URL = 'sqlite:///./appointments.db'

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
    )

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declaractive_base()
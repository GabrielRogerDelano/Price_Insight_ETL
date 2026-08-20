from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from config import DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()

from db import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    address_city = Column(String)
    email = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)

    
from db import Base
from sqlalchemy import Column, String, Integer, Float

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    category = Column(String)
    rating = Column(Float)
    reviews = Column(Integer)

    #comentei pq vi que pelo sqlalchemy ja tem isso implementado
    # def __init__(self, id, title, price, category, rating, reviews):
    #     self.id = id
    #     self.title = title
    #     self.price = price
    #     self.category = category
    #     self.rating = rating
    #     self.reviews = reviews


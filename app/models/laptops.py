
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship
class Laptop(Base):
    __tablename__ = 'laptops'
    laptop_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    ram = Column(String)
    cpu = Column(String)
    storage = Column(String)
    screen = Column(String)

    product = relationship('Product')

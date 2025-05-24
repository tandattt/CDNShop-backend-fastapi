
from sqlalchemy import Column, Integer, String, Float, ForeignKey,Text
from app.db.database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    brand_id = Column(Integer, ForeignKey('brands.brand_id'))
    stock_quantity = Column(Integer)
    url_img = Column(String)
    category = relationship('Category')
    brand = relationship('Brand')
    imgs = relationship('Img')
    views = relationship("ViewHistory")
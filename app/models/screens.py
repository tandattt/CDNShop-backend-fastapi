
from sqlalchemy import Column, Integer, String,Float, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship
class Screen(Base):
    __tablename__ = 'screens'

    screen_id = Column(Integer, primary_key=True, index=True)
    screen_type = Column(String)
    screen_size = Column(Float)
    resolution = Column(String)
    refresh_rate = Column(Integer)
    aspect_ratio = Column(String)
    touchscreen = Column(String)
    
    product_id = Column(Integer, ForeignKey('products.product_id'))
    
    product = relationship("Product")

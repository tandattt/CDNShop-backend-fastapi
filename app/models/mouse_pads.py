
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.db.database import Base
from sqlalchemy.orm import relationship
class MousePad(Base):
    __tablename__ = 'mouse_pads'
    mouse_pad_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    
    material = Column(String)
    size = Column(String)
    color = Column(String)
    product = relationship('Product')

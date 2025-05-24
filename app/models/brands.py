
from sqlalchemy import Column, Integer, String
from app.db.database import Base
from sqlalchemy.orm import relationship
class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    
    product = relationship('Product')

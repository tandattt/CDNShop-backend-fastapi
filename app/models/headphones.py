
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship
class Headphone(Base):
    __tablename__ = 'headphones'
    headphone_id = Column(Integer,primary_key=True,index=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    # type = Column(String)
    connectivity_type = Column(String)
    battery_life = Column(String)
    color = Column(String)

    product = relationship('Product')

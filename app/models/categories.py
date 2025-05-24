
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

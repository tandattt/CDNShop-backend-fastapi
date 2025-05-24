
from sqlalchemy import Column, Integer, String,CHAR
import uuid
from app.db.database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    views = relationship("ViewHistory")
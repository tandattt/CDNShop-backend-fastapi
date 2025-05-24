
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    name: str
    email: str
    phone: str
    address: str

class UserCreate(UserBase):
    password: str
    role: str = 'user'
class User(UserBase):
    user_id: str

    class Config:
        orm_mode = True
class UserLogin(BaseModel):
    username: str
    password: str
    website: str
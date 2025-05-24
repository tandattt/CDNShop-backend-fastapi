
from pydantic import BaseModel
from typing import Optional

class LaptopBase(BaseModel):
    ram: str
    cpu: str
    storage: str
    screen: str

class LaptopCreate(LaptopBase):
    product_id: int

class Laptop(LaptopBase):
    product_id: int

    class Config:
        orm_mode = True

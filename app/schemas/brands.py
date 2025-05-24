
from pydantic import BaseModel

class BrandBase(BaseModel):
    name: str
    description: str

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    brand_id: int

    class Config:
        orm_mode = True

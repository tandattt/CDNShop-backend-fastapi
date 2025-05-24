
from pydantic import BaseModel

class HeadphoneBase(BaseModel):
    type: str
    connectivity_type: str
    battery_life: str
    color: str

class HeadphoneCreate(HeadphoneBase):
    pass

class Headphone(HeadphoneBase):
    product_id: int

    class Config:
        orm_mode = True

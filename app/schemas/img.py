from pydantic import BaseModel
from typing import Optional


class ImgBase(BaseModel):
    url: str
    product_id: int


class ImgCreate(ImgBase):
    pass


class ImgResponse(ImgBase):
    id: int

    class Config:
        orm_mode = True

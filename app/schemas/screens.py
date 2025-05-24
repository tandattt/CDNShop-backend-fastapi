
from pydantic import BaseModel

class ScreenBase(BaseModel):
    screen_type: str
    screen_size: float
    resolution: str
    refresh_rate: int
    aspect_ratio: str
    touchscreen: str

class ScreenCreate(ScreenBase):
    pass

class Screen(ScreenBase):
    screen_id: int

    class Config:
        orm_mode = True

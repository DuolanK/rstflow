from datetime import datetime
from pydantic import BaseModel

class ShopCreate(BaseModel):
    name: str
    description: str
    creator_id: int
    is_active: bool
    work_time_from: DateTime.Time
    work_time_to: DateTime.Time
    latitude: float
    longitude: float


class ShopUpdate(BaseModel):
    name: str
    description: str
    creator_id: int
    is_active: bool
    work_time_from: DateTime.Time
    work_time_to: DateTime.Time
    latitude: float
    longitude: float

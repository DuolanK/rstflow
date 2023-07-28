from datetime import datetime
from pydantic import BaseModel

class ShopCreate(BaseModel):
    name: str
    description: str
    creator_id: int

class ShopUpdate(BaseModel):
    name: str
    description: str
    creator_id: int


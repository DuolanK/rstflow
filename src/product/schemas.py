from datetime import datetime
from pydantic import BaseModel

class ProductCreate(BaseModel):
    shop_id: int
    quantity: int
    price: int
    name: str
    date: datetime
    time: int
    description: str
    is_available: bool


class ProductUpdate(BaseModel):
    shop_id: int
    quantity: int
    price: int
    name: str
    date: datetime
    time: int
    description: str
    is_available: bool


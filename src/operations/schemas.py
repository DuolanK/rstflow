from datetime import datetime
from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    quantity: int
    price: int
    creator_id: int
    name: str
    date: datetime
    time: int
    description: str


class ProductUpdate(BaseModel):
    id: int
    quantity: int
    price: int
    creator_id: int
    name: str
    date: datetime
    time: int
    description: str



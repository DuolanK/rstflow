from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    quantity: str
    price: str
    creator_id: int
    name: str
    date: datetime
    time: int
    description: str


class ProductUpdate(BaseModel):
    id: int
    quantity: str
    price: str
    creator_id: int
    name: str
    date: datetime
    time: int
    description: str



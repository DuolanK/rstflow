from datetime import datetime

from pydantic import BaseModel


class OrderCreate(BaseModel):
    id: int
    quantity: int
    creator: str
    date: datetime




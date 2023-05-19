from datetime import datetime

from pydantic import BaseModel


class OrderCreate(BaseModel):
    id: int
    quantity: int
    creator_id: int
    date: datetime




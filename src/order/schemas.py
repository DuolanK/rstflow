from datetime import datetime
from pydantic import BaseModel


class OrderCreate(BaseModel):
    id: int
    quantity: int
    shop_id: int
    client_id: int
    date: datetime




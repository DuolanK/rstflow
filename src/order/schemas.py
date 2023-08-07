from datetime import datetime
from pydantic import BaseModel


class OrderCreate(BaseModel):
    quantity: int
    shop_id: int
    client_id: int
    created_at: datetime
    done_until: datetime
    status_id: int


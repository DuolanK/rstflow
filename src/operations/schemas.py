from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    name: str
    instrument_type: str
    date: datetime
    description: str
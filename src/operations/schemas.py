from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    name: str
    date: datetime
    description: str


class OperationUpdate(BaseModel):
    quantity: str
    name: str
    date: datetime
    description: str

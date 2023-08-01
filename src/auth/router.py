from fastapi import APIRouter, Depends, Request
from .base_config import current_active_user
from .models import User



router = APIRouter(
    prefix="/authapi",
    tags=["authapi"]
)


@router.get("/jwt")
def protected_route(user: User = Depends(current_active_user)):
    return {"user_id": user.id}
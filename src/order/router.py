from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .models import order
from .schemas import OrderCreate
from fastapi.responses import JSONResponse
from auth.base_config import current_active_user
from auth.models import User

router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/")
async def get_specific_product(order_id: int, user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.order == order_id)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.post("/")
async def add_specific_product(new_order: OrderCreate, user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/main")
async def get_all_products(user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)):
    query = select(order)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]
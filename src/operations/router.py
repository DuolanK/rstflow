
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import operation
from .schemas import OperationCreate
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_description: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.description == operation_description)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/main")
async def get_all_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(operation)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]
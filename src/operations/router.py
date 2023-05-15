from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import operation
from .schemas import OperationCreate, OperationUpdate
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


@router.put("/{operation_id}")
async def update_specific_operation(id: int, updated_operation: OperationUpdate, session: AsyncSession = Depends(get_async_session)):
    # Проверка, существует ли операция с указанным идентификатором
    existing_operation = await session.execute(select(operation).filter_by(id=id))
    if not existing_operation.scalar():
        raise HTTPException(status_code=404, detail="Записьне найдена")

    # Обновление информации об операции
    update_values = updated_operation.dict(exclude_unset=True)
    await session.execute(update(operation).where(operation.c.id == id).values(**update_values))
    await session.commit()

    return {"status": "success"}

@router.delete("/{operation_id}")
async def delete_specific_operation(id: int, session: AsyncSession = Depends(get_async_session)):
    # Проверка, существует ли операция с указанным идентификатором
    existing_operation = await session.execute(select(operation).filter_by(id=id))
    if not existing_operation.scalar():
        raise HTTPException(status_code=404, detail="<Запись> не найдена")

    # Удаление операции
    await session.execute(delete(operation).where(operation.c.id == id))
    await session.commit()

    return {"status": "success"}



@router.get("/main")
async def get_all_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(operation)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]
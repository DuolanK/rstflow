from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import product
from .schemas import ProductCreate, ProductUpdate
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/")
async def get_specific_product(product_description: str, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.description == product_description)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.post("/")
async def add_specific_product(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{product_id}")
async def update_specific_product(id: int, updated_product: ProductUpdate, session: AsyncSession = Depends(get_async_session)):
    # Проверка, существует ли операция с указанным идентификатором
    existing_product = await session.execute(select(product).filter_by(id=id))
    if not existing_product.scalar():
        raise HTTPException(status_code=404, detail="Записьне найдена")

    # Обновление информации об операции
    update_values = updated_product.dict(exclude_unset=True)
    await session.execute(update(product).where(product.c.id == id).values(**update_values))
    await session.commit()

    return {"status": "success"}

@router.delete("/{product_id}")
async def delete_specific_product(id: int, session: AsyncSession = Depends(get_async_session)):
    # Проверка, существует ли операция с указанным идентификатором
    existing_product = await session.execute(select(product).filter_by(id=id))
    if not existing_product.scalar():
        raise HTTPException(status_code=404, detail="<Запись> не найдена")

    # Удаление операции
    await session.execute(delete(product).where(product.c.id == id))
    await session.commit()

    return {"status": "success"}



@router.get("/main")
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    query = select(product)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]
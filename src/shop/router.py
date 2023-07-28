from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .models import shop
from .schemas import ShopCreate, ShopUpdate
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/shop",
    tags=["Shops"]
)

@router.get("/")
async def get_specific_shop(shop_description: str, session: AsyncSession = Depends(get_async_session)):
    query = select(shop).where(shop.c.description == shop_description)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.post("/")
async def add_specific_shop(new_shop: ShopCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(shop).values(**new_shop.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{shop_id}")
async def update_specific_shop(id: int, updated_shop: ShopUpdate, session: AsyncSession = Depends(get_async_session)):
    # Проверка, существует ли операция с указанным идентификатором
    existing_shop = await session.execute(select(shop).filter_by(id=id))
    if not existing_shop.scalar():
        raise HTTPException(status_code=404, detail="<Запись> о магазине не найдена")

    # Обновление информации об операции
    update_values = updated_shop.dict(exclude_unset=True)
    await session.execute(update(shop).where(shop.c.id == id).values(**update_values))
    await session.commit()

    return {"status": "success"}

@router.delete("/{shop_id}")
async def delete_specific_shop(id: int, session: AsyncSession = Depends(get_async_session)):
    # Проверка, существует ли операция с указанным идентификатором
    existing_shop = await session.execute(select(shop).filter_by(id=id))
    if not existing_shop.scalar():
        raise HTTPException(status_code=404, detail="<Запись> о магазине не найдена")

    # Удаление операции
    await session.execute(delete(shop).where(shop.c.id == id))
    await session.commit()

    return {"status": "success"}


@router.get("/main")
async def get_all_shops(session: AsyncSession = Depends(get_async_session)):
    query = select(shop)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]
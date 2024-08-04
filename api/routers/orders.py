import datetime as dt
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import orders as schemas
from database.db import get_async_session
from database.models import Order
from repositories import dogs as dogs_repo
from repositories import orders as orders_repo
from repositories import walkers as walkers_repo

router = APIRouter(prefix='/orders', tags=['orders'])
db_session = Annotated[AsyncSession, Depends(get_async_session)]


@router.get('/{date}', response_model=list[schemas.Order])
async def get_orders_by_date(db: db_session, date: dt.date) -> list[Order]:
    return await orders_repo.get_orders_by_date(db, date)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Order)
async def create_order(db: db_session, order_data: schemas.CreateOrder) -> Order:
    free_walker = await walkers_repo.get_free_walker(db, order_data.walk_at)
    if free_walker is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='There is no free dog walkers available at this datetime',
        )

    dog = await dogs_repo.get_or_create_dog(
        db, flat=order_data.flat, name=order_data.dog_name, breed=order_data.dog_breed
    )

    existing_order = await orders_repo.get_order(db, dog.id, order_data.walk_at)
    if existing_order:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='You have already booked a walk for this dog',
        )

    new_order = Order(
        dog_walker_id=free_walker.id,
        dog_id=dog.id,
        walk_at=order_data.walk_at,
    )
    db.add(new_order)
    await db.commit()
    return new_order

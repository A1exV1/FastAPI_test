import datetime as dt

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Order


async def get_orders_by_date(db: AsyncSession, date: dt.date) -> list[Order]:
    orders = await db.scalars(sa.select(Order).where(sa.func.DATE(Order.walk_at) == date))
    return list(orders.all())


async def get_order(db: AsyncSession, dog_id: int, walk_id: dt.datetime) -> Order | None:
    return await db.scalar(sa.select(Order).where(Order.dog_id == dog_id, Order.walk_at == walk_id))

import datetime as dt

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Order, Walker


async def get_free_walker(db: AsyncSession, walk_at: dt.datetime) -> Walker | None:
    query = (
        sa.select(Walker)
        .join(
            Order,
            sa.and_(Order.dog_walker_id == Walker.id, Order.walk_at == walk_at),
            isouter=True,
        )
        .where(Order.dog_walker_id.is_(None))
    )
    return await db.scalar(query)

from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Dog


async def get_or_create_dog(db: AsyncSession, **dog_data) -> Dog:
    query = (
        pg_insert(Dog)
        .values(**dog_data)
        .on_conflict_do_update(index_elements=['flat', 'name'], set_=dog_data)
        .returning(Dog)
    )

    return await db.scalar(query)

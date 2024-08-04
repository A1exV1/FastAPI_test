from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from common.settings import settings

engine = create_async_engine(settings.DATABASE_URI)

Session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncSession:
    async with Session() as session:
        yield session

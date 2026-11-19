from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlmodel import SQLModel

# 数据库地址
DATABASE_URL = 'sqlite+aiosqlite:///./books.db'

# 引擎
engine = create_async_engine(
    DATABASE_URL,
    echo = True,
    future = True
)

# 异步工厂
async_session = async_sessionmaker(
    engine,
    class_ = AsyncSession,
    expire_on_commit=False
)

# 工厂调用
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# 初始化数据库
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)



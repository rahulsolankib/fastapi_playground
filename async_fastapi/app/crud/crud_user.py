from typing import Optional
from sqlalchemy import String
from sqlalchemy.schema import CreateTable, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db.session import engine
import asyncio
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

# Base.metadata.create_all(engine)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())
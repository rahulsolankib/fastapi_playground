from fastapi import Depends
from typing import Annotated
from db.session import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


DBSession = Annotated[AsyncSession, Depends(get_db)]

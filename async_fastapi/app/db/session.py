from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

engine = create_async_engine(url=settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    expire_on_commit=False, class_=AsyncSession, bind=engine
)

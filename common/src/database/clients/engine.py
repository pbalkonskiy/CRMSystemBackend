"""Module with database engine setup."""

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


def get_engine(database_uri: str, echo: bool = False) -> AsyncEngine:
    """Initializes database async engine."""

    return create_async_engine(
        database_uri,
        echo=echo,
        pool_use_lifo=True,
        pool_pre_ping=True,
        pool_recycle=3600,
        pool_size=5,
    )

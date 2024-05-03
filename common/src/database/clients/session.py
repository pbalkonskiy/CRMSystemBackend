"""Module with async session setup and the related context manager."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker

from common.src.database.clients.engine import get_engine


@asynccontextmanager
async def get_async_session(
        connection_string: str,
        echo: bool,
) -> AsyncGenerator:
    """Async session context manager. Catches errors."""

    if not connection_string:
        raise ConnectionError("Database Session: No connection string set.")

    async_session = async_sessionmaker(
        bind=get_engine(connection_string, echo),
        expire_on_commit=False,
    )
    async_database_session = async_session()

    try:
        yield async_database_session
        await async_database_session.commit()
    except Exception as exception:
        await async_database_session.rollback()
        raise exception
    finally:
        await async_database_session.close()

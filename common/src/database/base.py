"""Base database core classes."""
from typing import Any

from sqlalchemy import JSON, inspect
from sqlalchemy.orm import DeclarativeBase


class DataBase(DeclarativeBase):
    """Inherited from ORM Declarative Base."""

    type_annotation_map = {
        dict[str, Any]: JSON
    }


class BaseModel(DataBase):
    """Base database model definition."""

    __abstract__ = True

    def as_dict(self) -> dict:
        """Serialize any model to a Python dictionary collection."""
        return {
            column.key: getattr(self, column.key) for column in
            inspect(self).mapper.column_attrs
        }

"""
Database initialization and session management.

This module is the single entry point for all database access.
Other modules should obtain database sessions through
`get_session()` and should never access the SQLAlchemy engine
directly.
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from database.models import Base

# -----------------------------------------------------------------------------
# Database Configuration
# -----------------------------------------------------------------------------

DATABASE_FILENAME = "pixel_backup.db"
DATABASE_PATH = Path(DATABASE_FILENAME)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# -----------------------------------------------------------------------------
# Engine
# -----------------------------------------------------------------------------

_engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

# -----------------------------------------------------------------------------
# Session Factory
# -----------------------------------------------------------------------------

_SessionFactory = sessionmaker(
    bind=_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------


def create_database() -> None:
    """
    Create all database tables if they do not already exist.
    """
    Base.metadata.create_all(_engine)


@contextmanager
def get_session() -> Iterator[Session]:
    """
    Provide a transactional SQLAlchemy session.

    The session is automatically committed if no exception occurs,
    otherwise it is rolled back.

    Example:
        with get_session() as session:
            ...
    """

    session = _SessionFactory()

    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()

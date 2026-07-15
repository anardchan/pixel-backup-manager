"""
SQLAlchemy database models.

These models are responsible only for persistence and should not be used
directly by the application logic. Domain models live in the `models`
package.
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Enum, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models.enums import BackupState, FileStatus


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    pass


class MediaFileRecord(Base):
    """
    Database representation of a media file.
    """

    __tablename__ = "media_files"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    source_path: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    status: Mapped[FileStatus] = mapped_column(
        Enum(FileStatus),
        nullable=False,
    )

    file_hash: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )


class BackupJobRecord(Base):
    """
    Database representation of a backup job.
    """

    __tablename__ = "backup_jobs"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    state: Mapped[BackupState] = mapped_column(
        Enum(BackupState),
        nullable=False,
    )

    file_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_size: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

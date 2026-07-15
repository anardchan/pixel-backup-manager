"""
Domain model representing a media file managed by the backup system.

This class is intentionally independent of:
- SQLite
- ADB
- Google Photos
- Rich UI
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from uuid import UUID, uuid4

from models.enums import FileStatus

BYTES_PER_MB = 1024**2
BYTES_PER_GB = 1024**3


@dataclass(slots=True)
class MediaFile:
    """
    Represents a media file managed by the backup system.

    This model is independent of the database, UI, and transfer engine.
    """

    id: UUID = field(default_factory=uuid4)

    source_path: Path

    size: int

    status: FileStatus = FileStatus.DISCOVERED

    file_hash: str | None = None

    def __post_init__(self) -> None:
        """Validate the media file."""

        if self.size < 0:
            raise ValueError("File size cannot be negative.")

        if not self.source_path.is_absolute():
            raise ValueError("source_path must be an absolute path.")

    @property
    def filename(self) -> str:
        """Filename including extension."""
        return self.source_path.name

    @property
    def extension(self) -> str:
        """File extension in lowercase."""
        return self.source_path.suffix.lower()

    @property
    def parent(self) -> Path:
        """Parent directory."""
        return self.source_path.parent

    @property
    def exists(self) -> bool:
        """Returns True if the file currently exists."""
        return self.source_path.exists()

    @property
    def size_mb(self) -> float:
        """File size in MiB."""
        return self.size / (BYTES_PER_MB)

    @property
    def size_gb(self) -> float:
        """File size in GiB."""
        return self.size / (BYTES_PER_GB)

    def __str__(self) -> str:
        """Human-readable representation."""
        return self.filename

from enum import StrEnum, auto


class FileStatus(StrEnum):
    """
    Represents the lifecycle of a single media file.
    """

    DISCOVERED = auto()
    QUEUED = auto()

    TRANSFERRING = auto()
    ON_PHONE = auto()

    BACKING_UP = auto()
    BACKUP_COMPLETE = auto()

    VERIFIED = auto()

    LOCAL_DELETED = auto()

    FAILED = auto()

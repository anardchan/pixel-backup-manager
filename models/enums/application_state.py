from enum import StrEnum, auto


class ApplicationState(StrEnum):
    """
    High-level application state.
    """

    STARTING = auto()

    CONNECTING_PHONE = auto()

    SCANNING_FILES = auto()

    PLANNING_BATCH = auto()

    TRANSFERRING = auto()

    WAITING_FOR_BACKUP = auto()

    FREEING_SPACE = auto()

    VERIFYING = auto()

    DELETING_LOCAL_FILES = auto()

    COMPLETE = auto()

    ERROR = auto()

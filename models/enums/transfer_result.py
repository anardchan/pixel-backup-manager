from enum import StrEnum, auto


class TransferResult(StrEnum):
    SUCCESS = auto()

    FAILED = auto()

    SKIPPED = auto()

    RETRY = auto()

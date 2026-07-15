from enum import StrEnum, auto


class PhoneState(StrEnum):
    """
    Current phone connection state.
    """

    DISCONNECTED = auto()

    CONNECTING = auto()

    CONNECTED = auto()

    DEVICE_NOT_FOUND = auto()

    UNAUTHORIZED = auto()

    OFFLINE = auto()

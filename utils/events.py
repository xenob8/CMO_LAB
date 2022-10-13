from enum import Enum, auto


class Event(Enum):
    WAITING_SOURCE = auto()
    READY_SOURCE = auto()
    CANCELED = auto()
    IN_BUFFER = auto()
    READY_TO_SERVICE = auto()
    IN_INSTRUMENT = auto()
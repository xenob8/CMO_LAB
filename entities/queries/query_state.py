from enum import Enum, auto


class QueryState(Enum):
    FROM_SOURCE = auto()
    FROM_INSTRUMENT = auto()
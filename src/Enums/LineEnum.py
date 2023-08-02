from enum import Enum

class LineEnum(Enum):
    UNDEFINED = 0
    CLOSED_LINE = 1
    NOT_CLOSED_LINE = 2
    STRAIGHT = 3
    BROKE_LINE = 4
    CURVE_LINE = 5
    RAY = 6
    SEGMENT = 7

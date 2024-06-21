from enum import Enum


class MovementStates(Enum):
    NEXT_STEP=1
    COLUMN_AVAILABLE=2
    ROW_AVAILABLE=3
    NONIUS_AVAILABLE=4
    COMMON_AVAILABLE=5
    BEST_PICK=6
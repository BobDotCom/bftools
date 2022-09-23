from enum import Enum

__all__ = (
    "Code",
    "Symbol",
)


class Code(Enum):
    """Enum for python code from a :class:`.Symbol`."""

    SHIFTRIGHT = "shift_right({0})"
    SHIFTLEFT = "shift_left({0})"
    ADD = "increment({0})"
    SUBTRACT = "decrement({0})"
    STARTLOOP = "while not is_zero():"
    ENDLOOP = ""
    INPUT = "get_input()"
    OUTPUT = "output()"


class Symbol(Enum):
    """Enum for brainfuck symbols."""

    SHIFTRIGHT = ">"
    SHIFTLEFT = "<"
    ADD = "+"
    SUBTRACT = "-"
    STARTLOOP = "["
    ENDLOOP = "]"
    INPUT = ","
    OUTPUT = "."
    UNKNOWN = None

    @classmethod
    def _missing_(cls, value: object) -> "Symbol":
        return cls.UNKNOWN

from enum import Enum

__all__ = (
    "Code",
    "Symbol",
)


class Code(Enum):
    """Enum for python code from a :class:`.Symbol`."""

    SHIFTRIGHT = "main.shift_right({0})"
    SHIFTLEFT = "main.shift_left({0})"
    ADD = "main.increment({0})"
    SUBTRACT = "main.decrement({0})"
    STARTLOOP = "while not main.is_zero():"
    ENDLOOP = ""
    INPUT = "main.get_input()"
    OUTPUT = "main.output()"


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
    def _missing_(cls, value):
        return cls.UNKNOWN

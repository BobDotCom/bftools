from enum import Enum


class Code(Enum):
    """Enum for python code from a :class:`.Symbol`."""

    SHIFTRIGHT = "position += {0}"
    SHIFTLEFT = "position -= {0}"
    ADD = "main[position] += {0}"
    SUBTRACT = "main[position] -= {0}"
    STARTLOOP = "while main[position] != 0:"
    ENDLOOP = ""
    INPUT = "main[position] = ord(input())"
    OUTPUT = "print(chr(main[position]), end='')"


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

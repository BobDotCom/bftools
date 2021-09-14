from enum import Enum


class Code(Enum):
    SHIFTRIGHT = "position += 1"
    SHIFTLEFT = "position -= 1"
    ADD = "main[position] += 1"
    SUBTRACT = "main[position] -= 1"
    STARTLOOP = "while main[position] != 0:"
    ENDLOOP = ""
    INPUT = "main[position] = ord(input())"
    OUTPUT = "print(chr(main[position]), end='')"


class Symbol(Enum):
    SHIFTRIGHT = ">"
    SHIFTLEFT = "<"
    ADD = "+"
    SUBTRACT = "-"
    STARTLOOP = "["
    ENDLOOP = "]"
    INPUT = ","
    OUTPUT = "."

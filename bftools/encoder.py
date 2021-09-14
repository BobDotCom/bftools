from .tools import factor
from typing import Optional


class EncodedBrainfuck:
    def __init__(self):
        self._code: Optional[str] = None

    @property
    def code(self):
        return self._code

    def parse(self, text: str) -> None:
        self._code = ""
        for character in text:
            num = ord(character)
            added = 0
            factored = factor(num)
            while 1 in factored:  # a small bit of optimization
                added += 1
                factored = factor(num + added)
            self._code += f">{'+' * factored[0]}[<{'+' * factored[1]}>-]<{'-' * added}.>"

from typing import List, Tuple, Optional

from .enums import Symbol, Code


class ParsedBrainfuck:
    def __init__(self) -> None:
        self._main: List[int] = [0 for _ in range(10000)]
        self._position: int = 0
        self._raw_parsed: Optional[List[Symbol]] = []
        self._code: Optional[str] = None

    @property
    def code(self):
        return self._code

    @property
    def main(self) -> List[int]:
        return self._main

    @property
    def position(self) -> int:
        return self._position

    @property
    def raw_parsed(self) -> Tuple[Symbol]:
        if self._raw_parsed is None:
            raise ValueError("self._raw_parsed is None")
        return tuple(self._raw_parsed)

    pos = position

    def parse(self, code: str) -> None:
        self._raw_parsed = []
        for character in code:
            try:
                parsed = Symbol(character)
                self._raw_parsed.append(parsed)
            except ValueError:  # TODO: add support for comments
                # Since comments are not supported yet, let's just skip for now
                continue
        self._code = """# Compiled using bftools (https://github.com/BobDotCom/bftools)

# Initialization
main = [0 for _ in range(10000)]
position = 0

# Code from brainfuck
"""
        indentation = 0
        for symbol in self.raw_parsed:
            self._code += f"\n{' ' * 4 * indentation}{Code[symbol.name].value}"
            if symbol == Symbol.STARTLOOP:
                indentation += 1
            elif symbol == Symbol.ENDLOOP:
                indentation -= 1

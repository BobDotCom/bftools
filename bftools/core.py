from typing import *

from .parser import ParsedBrainfuck


class Compiler:
    def __init__(self) -> None:
        self._last_parsed: Optional[ParsedBrainfuck] = None

    @property
    def last_parsed(self) -> Optional[ParsedBrainfuck]:
        return self._last_parsed

    def _new_parser(self) -> ParsedBrainfuck:
        parser = ParsedBrainfuck()
        self._last_parsed = parser
        return parser

    def parse(self, code: str) -> ParsedBrainfuck:
        parser = self._new_parser()
        parser.parse(code)
        return parser

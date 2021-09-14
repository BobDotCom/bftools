from typing import *

from .parser import CompiledBrainfuck


class BrainfuckTools:
    def __init__(self) -> None:
        self._last_compiled: Optional[CompiledBrainfuck] = None

    @property
    def last_compiled(self) -> Optional[CompiledBrainfuck]:
        return self._last_compiled

    def _new_compiler(self) -> CompiledBrainfuck:
        compiler = CompiledBrainfuck()
        self._last_compiled = compiler
        return compiler

    def compile(self, code: str) -> CompiledBrainfuck:
        compiler = self._new_compiler()
        compiler.parse(code)
        return compiler

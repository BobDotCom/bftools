from typing import Optional

from .compiler import CompiledBrainfuck
from .encoder import EncodedBrainfuck


class BrainfuckTools:
    def __init__(self) -> None:
        self._last_compiled: Optional[CompiledBrainfuck] = None
        self._last_encoded: Optional[EncodedBrainfuck] = None

    @property
    def last_compiled(self) -> Optional[CompiledBrainfuck]:
        return self._last_compiled

    @property
    def last_encoded(self):
        return self._last_encoded

    def _new_compiler(self) -> CompiledBrainfuck:
        compiler = CompiledBrainfuck()
        self._last_compiled = compiler
        return compiler

    def _new_encoder(self) -> EncodedBrainfuck:
        encoder = EncodedBrainfuck()
        self._last_encoded = encoder
        return encoder

    def compile(self, code: str) -> CompiledBrainfuck:
        compiler = self._new_compiler()
        compiler.parse(code)
        return compiler

    def encode(self, text: str) -> EncodedBrainfuck:
        encoder = self._new_encoder()
        encoder.parse(text)
        return encoder

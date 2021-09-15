from typing import Optional

from .compiler import CompiledBrainfuck
from .decoder import DecodedBrainfuck
from .encoder import EncodedBrainfuck


class BrainfuckTools:
    def __init__(self) -> None:
        self._last_compiled: Optional[CompiledBrainfuck] = None
        self._last_decoded: Optional[DecodedBrainfuck] = None
        self._last_encoded: Optional[EncodedBrainfuck] = None

    @property
    def last_compiled(self) -> Optional[CompiledBrainfuck]:
        return self._last_compiled

    @property
    def last_decoded(self):
        return self._last_decoded

    @property
    def last_encoded(self):
        return self._last_encoded

    def _new_compiler(self) -> CompiledBrainfuck:
        compiler = CompiledBrainfuck()
        self._last_compiled = compiler
        return compiler

    def _new_decoder(self) -> DecodedBrainfuck:
        decoder = DecodedBrainfuck()
        self._last_decoded = decoder
        return decoder

    def _new_encoder(self) -> EncodedBrainfuck:
        encoder = EncodedBrainfuck()
        self._last_encoded = encoder
        return encoder

    def compile(self, code: str) -> CompiledBrainfuck:
        compiler = self._new_compiler()
        compiler.parse(code)
        return compiler

    def decode(self, code: str) -> DecodedBrainfuck:
        compiler = CompiledBrainfuck()
        compiler.parse(code)
        decoder = self._new_decoder()
        decoder.parse(compiler.code)
        return decoder

    def encode(self, text: str) -> EncodedBrainfuck:
        encoder = self._new_encoder()
        encoder.parse(text)
        return encoder

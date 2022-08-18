from typing import Optional

from .compiler import CompiledBrainfuck
from .decoder import DecodedBrainfuck
from .encoder import EncodedBrainfuck


class BrainfuckTools:
    """The BrainfuckTools class is a wrapper for the compiler, decoder and encoder methods.

    It comes with some tools
    to make it easier to use, such as caching the last compiled code, the last decoded code and the last encoded
    text.

    Attributes
    ----------
    last_compiled: Optional[CompiledBrainfuck]
        The last compiled code.
    last_decoded: Optional[DecodedBrainfuck]
        The last decoded code.
    last_encoded: Optional[EncodedBrainfuck]
        The last encoded text.
    """

    def __init__(self) -> None:
        self.last_compiled: Optional[CompiledBrainfuck] = None
        self.last_decoded: Optional[DecodedBrainfuck] = None
        self.last_encoded: Optional[EncodedBrainfuck] = None

    def _new_compiler(self) -> CompiledBrainfuck:
        compiler = CompiledBrainfuck()
        self.last_compiled = compiler
        return compiler

    def _new_decoder(self) -> DecodedBrainfuck:
        decoder = DecodedBrainfuck()
        self.last_decoded = decoder
        return decoder

    def _new_encoder(self) -> EncodedBrainfuck:
        encoder = EncodedBrainfuck()
        self.last_encoded = encoder
        return encoder

    def compile(self, code: str) -> CompiledBrainfuck:
        """
        Compiles a brainfuck code into python code.

        Parameters
        ----------
        code: str
            The brainfuck code to compile.

        Returns
        -------
        CompiledBrainfuck
            The compiled code.
        """
        compiler = self._new_compiler()
        compiler.parse(code)
        return compiler

    def decode(self, code: str) -> DecodedBrainfuck:
        """Decodes brainfuck code into text.

        Parameters
        ----------
        code: str
            The brainfuck code to decode.

        Returns
        -------
        DecodedBrainfuck
            The decoded code.
        """
        compiler = CompiledBrainfuck()
        compiler.parse(code)
        decoder = self._new_decoder()
        decoder.parse(compiler.result or "")
        return decoder

    def encode(self, text: str) -> EncodedBrainfuck:
        """Encodes text into brainfuck code.

        Parameters
        ----------
        text: str
            The text to encode.

        Returns
        -------
        EncodedBrainfuck
            The encoded text.
        """
        encoder = self._new_encoder()
        encoder.parse(text)
        return encoder


# Some shortcuts
def compile(code: str) -> CompiledBrainfuck:  # pylint: disable=redefined-builtin
    """Shortcut for :meth:`BrainfuckTools.compile`.

    This is equivalent to ``BrainfuckTools().compile(code)``.

    Parameters
    ----------
    code: str
        The brainfuck code to compile.

    Returns
    -------
    CompiledBrainfuck
        The compiled code.
    """
    return BrainfuckTools().compile(code)


def decode(code: str) -> DecodedBrainfuck:
    """Shortcut for :meth:`BrainfuckTools.decode`.

    This is equivalent to ``BrainfuckTools().decode(code)``.

    Parameters
    ----------
    code: str
        The brainfuck code to decode.

    Returns
    -------
    DecodedBrainfuck
        The decoded text.
    """
    return BrainfuckTools().decode(code)


def encode(text: str) -> EncodedBrainfuck:
    """Shortcut for :meth:`BrainfuckTools.encode`.

    This is equivalent to ``BrainfuckTools().encode(text)``.

    Parameters
    ----------
    text: str
        The text to encode.

    Returns
    -------
    EncodedBrainfuck
        The encoded text.
    """
    return BrainfuckTools().encode(text)

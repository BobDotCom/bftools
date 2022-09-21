from typing import List, Optional, Tuple

from .base import BrainfuckBase, HasSizes, IntegerSize
from .enums import Code, Symbol

__all__ = ("CompiledBrainfuck",)


class CompiledBrainfuck(BrainfuckBase, HasSizes):
    """An object to represent python compiled from Brainfuck.

    To receive the decoded text, use :attr:`result` or
    str(:class:`DecodedBrainfuck`).

    .. warning::
        This class is not intended to be instantiated directly. Use :func:`compile_bf` or :meth:`BrainfuckTools.compile`
        instead.

    Attributes
    ----------
    result: Optional[str]
        The result text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    def __init__(self, array_size: int = 30000, int_size: IntegerSize = 8) -> None:
        BrainfuckBase.__init__(self)
        HasSizes.__init__(self, array_size=array_size, int_size=int_size)
        self._raw_parsed: Optional[List[Symbol]] = []

    @property
    def raw_parsed(self) -> Optional[Tuple[Symbol, ...]]:
        """
        Raw parsed code.

        This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.

        .. note::
            This is meant to be used internally and you should not need to use it.

        Returns
        -------
        Optional[Tuple[Symbol]]
            The raw parsed code.
        """
        if self._raw_parsed is None:
            return None
        return tuple(self._raw_parsed)

    def parse(self, value: str) -> None:
        """Parse the given code.

        .. note::
            You should not need to use this method. It is intended for internal use only, so you should only need to use
            it if you override the functionality of the library. This method is not dangerous like
            :meth:`DecodedBrainfuck.parse` is.

        Parameters
        ----------
        value: str
            The code to parse.
        """
        self._raw_parsed = []
        for character in value:
            try:
                parsed = Symbol(character)
                self._raw_parsed.append(parsed)
            except ValueError:  # TODO: add support for comments
                # Since comments are not supported yet, let's just skip for now
                continue
        # TODO: Add correct IntegerSize typehints in compiled code
        self.result = f"""
import sys


class Main:
    def __init__(self, array_size: int = 30000, int_size: int = 8) -> None:
        self._size = array_size
        self._data = bytearray(self._size)
        self._position = 0
        self._int_size = int_size

    @property
    def array_size(self) -> int:
        return self._size

    @property
    def int_size(self) -> int:
        return self._int_size

    def shift_right(self, amount: int) -> None:
        self._position = (self._position + amount) % self._size

    def shift_left(self, amount: int) -> None:
        return self.shift_right(-amount)

    def _get_value(self) -> int:
        value = self._data[self._position]
        for i in range(1, self._int_size // 8):
            value += self._data[self._position + i] << (i * 8)
        return value

    def _set_value(self, value: int) -> None:
        self._data[self._position] = value & 0xFF
        for i in range(1, self._int_size // 8):
            self._data[self._position + i] = (value >> (i * 8)) & 0xFF

    def increment(self, amount: int) -> None:
        self._set_value((self._get_value() + amount) % (2 ** self._int_size))

    def decrement(self, amount: int) -> None:
        return self.increment(-amount)

    def is_zero(self) -> bool:
        return self._data[self._position] == 0

    def get_input(self) -> int:
        self._data[self._position] = ord(sys.stdin.read(1))

    def output(self) -> None:
        print(chr(self._get_value()), end='')


main = Main(array_size={self._array_size}, int_size={self._int_size})
"""

        indentation = 0
        stackable = (Symbol.SHIFTLEFT, Symbol.SHIFTRIGHT, Symbol.ADD, Symbol.SUBTRACT)
        stack_level = 0
        stack_type = None
        if self.raw_parsed is not None:
            for symbol in self.raw_parsed:
                if symbol in stackable and stack_type == symbol:
                    stack_level += 1
                    stack_type = symbol
                    continue
                if stack_level > 0:
                    self.result += (
                        f"\n{' ' * 4 * indentation}"
                        f"{Code[stack_type.name].value.format(stack_level)}"  # type: ignore[union-attr]
                    )
                    stack_level = 0
                if symbol in stackable:
                    stack_level += 1
                    stack_type = symbol
                    continue
                self.result += f"\n{' ' * 4 * indentation}{Code[symbol.name].value}"
                if symbol == Symbol.STARTLOOP:
                    indentation += 1
                elif symbol == Symbol.ENDLOOP:
                    indentation -= 1
        try:
            import python_minifier  # type: ignore # pylint: disable=import-outside-toplevel
        except ImportError:

            class Minifier:
                """
                Mock class for python_minifier.

                Does nothing.
                """

                @staticmethod
                def minify(
                    code_val: str, **kwargs: bool  # pylint: disable=unused-argument
                ) -> str:
                    """
                    Mock method for python_minifier.

                    Does nothing.
                    Parameters
                    ----------
                    code_val: str
                        The code to minify.
                    kwargs
                        The keyword arguments to pass to the method.

                    Returns
                    -------
                    str
                        Simply returns the value of "code_val".
                    """
                    return code_val

            python_minifier = Minifier
        self.result = python_minifier.minify(
            self.result,
            remove_literal_statements=True,
            rename_globals=True,
        )
        self.result = (
            "# Compiled using bftools (https://github.com/BobDotCom/bftools)\n"
            + (self.result or "")
        )

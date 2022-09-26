import inspect
import os
from typing import List, Optional, Tuple

from .base import BrainfuckBase, HasSizes, IntegerSize
from .enums import Code, Symbol

__all__ = ("CompiledBrainfuck",)

try:
    import python_minifier
except ImportError:
    python_minifier = None


def _handle_indentation(symbol: Symbol, indentation: int) -> int:
    if symbol == Symbol.STARTLOOP:
        indentation += 1
    elif symbol == Symbol.ENDLOOP:
        indentation -= 1
    return indentation


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
        self._comments = ""

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

    def _parse_raw(self, value: str) -> None:
        self._raw_parsed = []
        for character in value:
            parsed = Symbol(character)
            self._raw_parsed.append(parsed)
            if parsed == Symbol.UNKNOWN:
                self._comments += character

    def parse(
        self,
        value: str,
        minify: Optional[bool] = None,
    ) -> None:
        """Parse the given code.

        .. note::
            You should not need to use this method. It is intended for internal use only, so you should only need to use
            it if you override the functionality of the library. This method is not dangerous like
            :meth:`DecodedBrainfuck.parse` is.

        Parameters
        ----------
        value: str
            The code to parse.
        minify: Optional[bool]
            Whether to minify the code. If ``None``, this will be determined by whether :mod:`python_minifier` is
            installed.
        """
        self._parse_raw(value)
        # TODO: Add correct IntegerSize typehints in compiled code

        with open(
            os.path.join(os.path.dirname(__file__), "template.py"), encoding="utf-8"
        ) as file:
            self.result = file.read().format(self.array_size, self.int_size)
        #             self.result += f"""
        # main = Main(array_size={self.array_size}, int_size={self.int_size})
        # """
        indentation = 0
        stackable = (Symbol.SHIFTLEFT, Symbol.SHIFTRIGHT, Symbol.ADD, Symbol.SUBTRACT)
        stack_level = 0
        stack_type = None
        is_comment = False
        comments = iter(self._comments)
        for symbol in self.raw_parsed or []:
            if symbol in stackable and stack_type == symbol:
                stack_level += 1
                stack_type = symbol
                continue
            if symbol.name == "UNKNOWN":
                value = next(comments)
                if not is_comment:
                    # New comment. Unless it's a newline, we want to add a pound sign.
                    if value != "\n":
                        value = f"# {value}"
                    is_comment = True
            else:
                is_comment = False
                value = Code[symbol.name].value

            if stack_level > 0:
                new_value = Code[stack_type.name].value.format(stack_level)  # type: ignore[union-attr]
                stack_level = 0
                self.result += f"\n{' ' * 4 * indentation}{new_value}"

            if symbol in stackable:
                stack_level += 1
                stack_type = symbol
                continue

            try:
                # We're checking if there has been a newline since the last comment. The pound index needs to be
                # executed first, in case the first comment is on the first line. It's currently impossible for that
                # to happen, but it's good to be safe.
                pound_index = str.rindex(self.result, "#")
                is_continued_comment = is_comment
                if str.rindex(self.result, "\n") > pound_index:
                    is_continued_comment = False
            except ValueError:
                is_continued_comment = False
            if not is_continued_comment:
                value = f"\n{' ' * 4 * indentation}{value}"
            if value == "\n":
                is_comment = False
            self.result += value

            indentation = _handle_indentation(symbol, indentation)
        self._minify(minify)
        self.result = (
            "# Compiled using bftools (https://github.com/BobDotCom/bftools)\n"
            + (self.result or "")
        )

    def _minify(self, should_minify: Optional[bool] = True) -> None:
        if should_minify is None:
            should_minify = python_minifier is not None
        if not should_minify:
            return
        if python_minifier is None:
            raise ImportError("python_minifier is not installed")
        kwargs = []
        for key in ("remove_literal_statements", "rename_globals"):
            if key in inspect.signature(python_minifier.minify).parameters:
                kwargs.append(key)

        self.result = python_minifier.minify(
            self.result,
            **{key: True for key in kwargs},
        )

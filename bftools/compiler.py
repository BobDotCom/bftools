import warnings
from typing import List, Optional, Tuple

from .enums import Code, Symbol
from .exceptions import NotParsedException


class CompiledBrainfuck:
    """An object to represent python compiled from Brainfuck.

    To receive the decoded text, use :attr:`result` or
    str(:class:`DecodedBrainfuck`).

    .. warning::
        This class is not intended to be instantiated directly. Use :meth:`decode` or :meth:`BrainfuckTools.decode`
        instead.

    Attributes
    ----------
    result: Optional[str]
        The result code. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    # pylint: disable=duplicate-code
    # TODO: Use a base class to avoid duplicate code
    def __init__(self) -> None:
        self._raw_parsed: Optional[List[Symbol]] = []
        self.result: Optional[str] = None

    def __str__(self) -> str:
        if self.result is None:
            raise NotParsedException("The code has not been parsed yet.")

        return self.result

    @property
    def code(self) -> Optional[str]:
        """The compiled code.

        .. deprecated:: 0.3.0
            The code property is deprecated and will be removed in 0.5.0. Use :attr:`result` or
            str(:class:`CompiledBrainfuck`) instead.

        Returns
        -------
        Optional[str]
            The compiled code. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
            always calls :meth:`parse` before returning the object, this should never happen unless you override the
            functionality of the library.
        """
        warnings.warn(
            "The text property is deprecated since 0.3.0 and will be removed in 0.5.0. Use "
            "DecodedBrainfuck.result or str(DecodedBrainfuck) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.result

    @property
    def raw_parsed(self) -> Optional[Tuple[Symbol, ...]]:
        """
        Raw parsed code

        This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.

        .. note::
            This is meant to be used internally and you should not need to use it.

        .. versionchanged:: 0.3.0
            Now returns ``None`` instead of raising a ValueError.

        Returns
        -------
        Optional[Tuple[Symbol]]
            The raw parsed code.
        """
        if self._raw_parsed is None:
            return None
        return tuple(self._raw_parsed)

    def parse(self, code: str) -> None:
        """Parse the given code.

        .. note::
            You should not need to use this method. It is intended for internal use only, so you should only need to use
            it if you override the functionality of the library. This method is not dangerous like
            :meth:`DecodedBrainfuck.parse` is.

        Parameters
        ----------
        code: str
            The code to parse.
        """
        self._raw_parsed = []
        for character in code:
            try:
                parsed = Symbol(character)
                self._raw_parsed.append(parsed)
            except ValueError:  # TODO: add support for comments
                # Since comments are not supported yet, let's just skip for now
                continue
        self.result = """
main = bytearray(30000)
position = 0
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
                Mock class for python_minifier

                Does nothing.
                """

                @staticmethod
                def minify(
                    code_val: str, **kwargs: bool  # pylint: disable=unused-argument
                ) -> str:
                    """
                    Mock method for python_minifier

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

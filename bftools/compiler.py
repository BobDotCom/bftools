import warnings
from typing import List, Tuple, Optional

from .enums import Symbol, Code


class CompiledBrainfuck:
    def __init__(self) -> None:
        """An object to represent python compiled from Brainfuck. To recieve the decoded text, use :attr:`result` or
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
        self._raw_parsed: Optional[List[Symbol]] = []
        self.result: Optional[str] = None

    def __str__(self) -> str:
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
        warnings.warn("The text property is deprecated since 0.3.0 and will be removed in 0.5.0. Use "
                      "DecodedBrainfuck.result or str(DecodedBrainfuck) instead.", DeprecationWarning, stacklevel=2)
        return self.result

    @property
    def raw_parsed(self) -> Optional[Tuple[Symbol]]:
        """
        Raw parsed code. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
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
        self.result = """# Compiled using bftools (https://github.com/BobDotCom/bftools)

# Initialization
main = bytearray(10000)
position = 0

# Code from brainfuck
"""
        indentation = 0
        stackable = (Symbol.SHIFTLEFT, Symbol.SHIFTRIGHT, Symbol.ADD, Symbol.SUBTRACT)
        stack_level = 0
        stack_type = None
        for symbol in self.raw_parsed:
            if symbol in stackable and stack_type == symbol:
                stack_level += 1
                stack_type = symbol
                continue
            else:
                if stack_level > 0:
                    self.result += f"\n{' ' * 4 * indentation}{Code[stack_type.name].value.format(stack_level)}"
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

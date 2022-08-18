import warnings
from typing import Optional

from .exceptions import NotParsedException
from .tools import factor


class EncodedBrainfuck:
    """An object to represent text encoded into Brainfuck.

    To receive the encoded Brainfuck, use :attr:`result` or
    str(:class:`EncodedBrainfuck`).

    .. warning::
        This class is not intended to be instantiated directly. Use :meth:`encode` or :meth:`BrainfuckTools.encode`
        instead.

    Attributes
    ----------
    result: Optional[str]
        The result code. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    def __init__(self) -> None:
        self.result: Optional[str] = None

    def __str__(self) -> str:
        if self.result is None:
            raise NotParsedException("The code has not been parsed yet.")
        return self.result

    @property
    def code(self) -> Optional[str]:
        """The encoded code.

        .. deprecated:: 0.3.0
            The code property is deprecated and will be removed in 0.4.0. Use :attr:`result` or
            str(:class:`EncodedBrainfuck`) instead.

        Returns
        -------
        Optional[str]
            The encoded text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
            always calls :meth:`parse` before returning the object, this should never happen unless you override the
            functionality of the library.
        """
        warnings.warn(
            "The text property is deprecated since 0.3.0 and will be removed in 0.4.0. Use "
            "DecodedBrainfuck.result or str(DecodedBrainfuck) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.result

    def parse(self, text: str) -> None:
        """Parse the given text.

        .. note::
            You should not need to use this method. It is intended for internal use only, so you should only need to use
            it if you override the functionality of the library. This method is not dangerous like
            :meth:`DecodedBrainfuck.parse` is.

        .. note:
            The library currently does not use much optimization, but it will in the future. The
            current optimization simply factors the number into loops, so instead of "+++++++++++++++", it will become
            "+++[>+++++<-]". As the brainfuck code gets more advanced, this has room for even more optimization.
            Currently, it is planned to optimize the code further by recursively factoring the number into smaller
            numbers. For example, instead of factoring 10000 into ``100 * 100``, it will become
            ``(10 * 10) * (10 * 10)``. This is planned for v0.4.

        Parameters
        ----------
        text: str
            The text to parse.
        """
        # TODO: Optimize by factoring recursively
        self.result = ""
        for character in text:
            num = ord(character)
            added = 0
            factored = factor(num)
            while 1 in factored:  # Does this cause an error for prime numbers?
                added += 1
                factored = factor(num + added)
            self.result += (
                f">{'+' * factored[0]}[<{'+' * factored[1]}>-]<{'-' * added}.>"
            )

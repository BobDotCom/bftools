import io
import sys
import warnings
from typing import Optional

from .exceptions import NotParsedException


class DecodedBrainfuck:
    """An object to represent text decoded from Brainfuck.

    To receive the decoded text, use :attr:`result` or
    str(:class:`DecodedBrainfuck`).

    .. warning::
        This class is not intended to be instantiated directly. Use :meth:`decode` or :meth:`BrainfuckTools.decode`
        instead.

    Attributes
    ----------
    result: Optional[str]
        The result text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    # pylint: disable=duplicate-code
    def __init__(self) -> None:
        self.result: Optional[str] = None

    def __str__(self) -> str:
        if self.result is None:
            raise NotParsedException("The code has not been parsed yet.")
        return self.result

    @property
    def text(self) -> Optional[str]:
        """The decoded text.

        .. deprecated:: 0.3.0
            The text property is deprecated and will be removed in 0.5.0. Use :attr:`result` or
            str(:class:`DecodedBrainfuck`) instead.

        Returns
        -------
        Optional[str]
            The result text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
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

    def parse(self, code: str) -> None:
        """Parse the given code.

        .. note::
            You should not need to use this method. It is intended for internal use only, so you should only need to use
            it if you override the functionality of the library. See the warning below for more information.

        .. warning::
            This method uses the :func:`exec` function. It is therefore not safe to use this method with untrusted
            code. The library uses this internally and will ensure that user input is not directly passed to this
            method, unless you override the functionality of the library. If you invoke this method directly, you need
            to ensure that the code you pass is safe.

        Parameters
        ----------
        code: str
            The code to parse.

        Raises
        ------
        SyntaxError
            If the code is not syntactically correct.
        """
        code_out = io.StringIO()
        sys.stdout = code_out
        exec(code)  # pylint: disable=exec-used  # nosec B102
        sys.stdout = sys.__stdout__
        out = code_out.getvalue()
        code_out.close()
        self.result = out

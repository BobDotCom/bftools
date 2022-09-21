import io
import sys

from .base import BrainfuckBase

__all__ = ("DecodedBrainfuck",)


class DecodedBrainfuck(BrainfuckBase):
    """An object to represent text decoded from Brainfuck.

    To receive the decoded text, use :attr:`result` or
    str(:class:`DecodedBrainfuck`).

    .. warning::
        This class is not intended to be instantiated directly. Use :func:`decode_bf` or :meth:`BrainfuckTools.decode`
        instead.

    Attributes
    ----------
    result: Optional[str]
        The result text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    def parse(self, value: str) -> None:
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
        value: str
            The code to parse.

        Raises
        ------
        SyntaxError
            If the code is not syntactically correct.
        """
        # TODO: Override builtin print function instead of capturing stdout
        code_out = io.StringIO()
        sys.stdout = code_out
        exec(value)  # pylint: disable=exec-used  # nosec B102
        sys.stdout = sys.__stdout__
        out = code_out.getvalue()
        code_out.close()
        self.result = out

# pylint: disable=unnecessary-ellipsis
class BfException(Exception):
    """Base exception class for bftools.

    It is used to catch any custom exception thrown by the library.
    """

    ...


class NotParsedException(BfException):
    """Exception raised when the input data has not been parsed yet."""

    ...

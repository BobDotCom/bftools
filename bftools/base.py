import sys
from abc import ABC, abstractmethod
from typing import Optional

from .exceptions import NotParsedException

if sys.version_info >= (3, 8):
    from typing import Literal
else:  # pragma: no cover
    from typing_extensions import Literal


__all__ = (
    "BrainfuckBase",
    "IntegerSize",
    "HasSizes",
)

IntegerSize = Literal[8, 16, 32, 64]


class BrainfuckBase(ABC):
    """A base class that is inherited by other classes.

    Attributes
    ----------
    result: Optional[str]
        The result text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    def __init__(self) -> None:
        self.result: Optional[str] = None

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        """Return the result text."""
        if self.result is None:
            raise NotParsedException("The code has not been parsed yet.")

        return self.result

    @abstractmethod
    def parse(self, value: str) -> None:
        """Should parse the given value."""
        raise NotImplementedError(
            "This method should be implemented by inheriting classes."
        )


class HasSizes(ABC):
    """A class that has sizes."""

    def __init__(self, array_size: int = 30000, int_size: IntegerSize = 8) -> None:
        self._array_size = array_size
        self._int_size = int_size

    @property
    def array_size(self) -> int:
        """The size of the array."""
        return self._array_size

    @property
    def int_size(self) -> IntegerSize:
        """The amount of bits per integer."""
        return self._int_size

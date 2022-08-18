import math
from typing import Tuple


def factor(x: int) -> Tuple[int, int]:  # pylint: disable=invalid-name
    """
    Factors :attr:`x` into 2 numbers, a and b, such that a + b is as small as possible.


    Parameters
    -----------
    x: :class:`int`
        The number to factor

    Returns
    --------
    Tuple[:class:`int`, :class:`int`]
        A Tuple of 2 integers that factor into :attr:`x`.
    """
    root_x = int(math.sqrt(x))
    for i in range(0, root_x):
        if x % (root_x + i) == 0:
            return root_x + i, x // (root_x + i)
        if x % (root_x - i) == 0:
            return root_x - i, x // (root_x - i)
    return x, 1

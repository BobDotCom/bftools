import math
from typing import Tuple


def factor(x: int) -> Tuple[int, int]:
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
    rt = int(math.sqrt(x))
    for i in range(0, rt):
        if x % (rt + i) == 0:
            return rt + i, x // (rt + i)
        if x % (rt - i) == 0:
            return rt - i, x // (rt - i)
    return x, 1

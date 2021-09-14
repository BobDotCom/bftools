from typing import Tuple


def factor(x: int) -> Tuple[int]:
    """
    Factors :param:`x` into 2 numbers, a and b, such that a + b
    is as small as possible.


    Parameters
    -----------
    x: :class:`int`
        The number to factor

    Returns
    --------
    Tuple[:class:`int`]
        A Tuple of 2 integers that factor into :param:`x`.
    """
    # let's do this by brute force cuz i'm lazy
    maximum = x // 2
    possible = {}
    for a in range(1, maximum):
        b = x / a
        if a * int(b) == x:
            b = int(b)
            possible.setdefault(a + b, set()).add((a, b))
    least = possible[min(possible)]
    possible = {}
    for a, b in least:
        possible[abs(a - b)] = (a, b)
    least = possible[min(possible)]
    return least

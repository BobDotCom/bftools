import math
from typing import Tuple

from .base import IntegerSize

__all__ = (
    "factor",
    "factor_recursive",
    "factor_optimized",
)


def factor_optimized(number: int, int_size: IntegerSize) -> Tuple[int, ...]:
    """
    An optimized factoring algorithm that factors :attr:`number` into the best combination of numbers to be compiled
    into brainfuck loops.

    This function leverages integer overflow to further shorten the code.

    Parameters
    -----------
    number: :class:`int`
        The number to factor
    int_size: :class:`IntegerSize`
        The size of the integer. This is used to optimize the factorization with integer overflow.

    Returns
    --------
    Tuple[:class:`int`, ...]
        A Tuple of integers that factor into :attr:`number`.
    """
    int_limit = 2**int_size
    number = number % int_limit
    if number == 0:
        return 0, 0
    if number < int_limit / 2:
        return factor_recursive(number)
    result = list(factor_recursive(int_limit - number))
    # Invert the largest number and return
    return (-result.pop(result.index(max(result))),) + tuple(result)


def factor(number: int) -> Tuple[int, int]:
    """
    Factors :attr:`number` into 2 numbers, a and b, such that a + b is as low as possible.

    Parameters
    -----------
    number: :class:`int`
        The number to factor

    Returns
    --------
    Tuple[:class:`int`, :class:`int`]
        A Tuple of 2 integers that factor into :attr:`number`.
    """
    root = int(math.sqrt(number))
    for i in range(0, root):
        if number % (root + i) == 0:
            return root + i, number // (root + i)
        if number % (root - i) == 0:
            return root - i, number // (root - i)
    return number, 1


def factor_recursive(number: int) -> Tuple[int, ...]:
    """
    Factors :attr:`number` into an undetermined amount of numbers, such that the accumulative sum of those numbers is as
    low as possible.

    Parameters
    -----------
    number: :class:`int`
        The number to factor

    Returns
    --------
    Tuple[:class:`int`, ...]
        A Tuple of integers that factor into :attr:`number`.
    """

    def inner(num: int) -> Tuple[int, ...]:
        first, second = factor(num)
        if first == 1:
            return (second,)
        if second == 1:
            return (first,)
        inner_result = inner(first) + inner(second)
        # Each time we factor, it adds 7 extra characters to the code
        if sum(inner_result) < len(inner_result) * 7:
            return inner_result
        return (num,)

    if (result := inner(number)) == ():
        result = (1,)

    if (count := result.count(2) // 2) > 0:
        temp = list(result)
        for _ in range(count):
            temp.remove(2)
            temp.remove(2)
            temp.append(4)
        result = tuple(temp)

    return result

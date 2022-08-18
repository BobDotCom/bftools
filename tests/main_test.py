import random
import string

import pytest

import bftools

tests = [
    "".join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(100)
]

numbers = (
    [random.randint(1, 10000) for _ in range(5)]  # Random numbers
    + [random.randint(1, 100) ** 2 for _ in range(5)]  # Squares
    + [0]
)


@pytest.fixture
def compiler():
    """Returns a compiler."""
    return bftools.BrainfuckTools()


@pytest.mark.parametrize("code", tests)
def test_conversions(compiler, code):
    assert compiler and code  # TODO: make tests


@pytest.mark.parametrize("num", numbers)
def test_factor(num):
    a, b = bftools.factor(num)
    assert a * b == num

import bftools
import pytest
import random
import string


tests = [''.join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(1000)]


@pytest.fixture
def compiler():
    """Returns a compiler"""
    return bftools.Compiler()


@pytest.mark.parametrize("code", tests)
def test_conversions(compiler, code):
    assert compiler and code  # TODO: make tests

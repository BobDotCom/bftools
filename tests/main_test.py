import io
import random
import string
import sys

import pytest

import bftools

tests = [
    "".join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(10)
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


def run_conversion_test(comp, code):
    val = "".join(random.choice(string.ascii_letters) for _ in range(10))
    assert str(comp.decode(str(comp.encode(code)) + val)) == code
    code_out = io.StringIO()
    sys.stdout = code_out
    exec(  # pylint: disable=exec-used  # nosec B102
        str(comp.compile(str(comp.encode(code))))
    )
    sys.stdout = sys.__stdout__
    out = code_out.getvalue()
    code_out.close()
    assert out == code


@pytest.mark.parametrize("code", tests)
def test_conversions(compiler, code):
    run_conversion_test(compiler, code)
    run_conversion_test(bftools, code)


@pytest.mark.parametrize("num", numbers)
def test_factor(num):
    a, b = bftools.factor(num)
    assert a * b == num


@pytest.mark.parametrize(
    "bf_obj",
    [
        bftools.DecodedBrainfuck(),
        bftools.CompiledBrainfuck(),
        bftools.EncodedBrainfuck(),
    ],
)
def test_not_parsed(bf_obj):
    with pytest.raises(bftools.NotParsedException):
        str(bf_obj)
    value = "".join(random.choice(string.ascii_letters) for _ in range(10))
    bf_obj.result = value
    assert str(bf_obj) == value


def test_raw_parsed():
    bf_obj = bftools.CompiledBrainfuck()
    bf_obj._raw_parsed = None
    assert bf_obj.raw_parsed is None

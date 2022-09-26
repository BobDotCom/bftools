import io
import random
import string
import sys
from typing import IO, Optional

import pytest

import bftools
from bftools import (
    CompiledBrainfuck,
    DecodedBrainfuck,
    EncodedBrainfuck,
    HasSizes,
    IntegerSize,
)


class MockCompiler(HasSizes):
    def __init__(self, array_size: int = 30000, int_size: IntegerSize = 8) -> None:
        super().__init__(array_size=array_size, int_size=int_size)
        self._module = bftools

    def compile(self, value: str) -> CompiledBrainfuck:
        return self._module.compile_bf(value)

    def decode(self, value: str) -> DecodedBrainfuck:
        return self._module.decode_bf(value)

    def encode(self, value: str) -> EncodedBrainfuck:
        return self._module.encode_text(value)


@pytest.fixture(params=range(2))
def array_size():
    return random.randint(10000, 100000)


@pytest.fixture(params=[8, 16, 32, 64])
def int_size(request):
    return request.param or None


@pytest.fixture(params=[bftools.BrainfuckTools, MockCompiler])
def compiler(request, array_size, int_size):
    """Returns a compiler."""
    return request.param(array_size=array_size, int_size=int_size)


def run_conversion_test(comp, code):
    val = "".join(random.choice(string.ascii_letters) for _ in range(10))
    assert str(comp.decode(str(comp.encode(code)) + val)) == code
    code_out = io.StringIO()

    def _print(
        *values: object,
        sep: Optional[str] = " ",
        end: Optional[str] = "\n",
        file: Optional[IO[str]] = code_out,
        flush: bool = False
    ) -> None:
        print(*values, sep=sep, end=end, file=file, flush=flush)

    exec(  # pylint: disable=exec-used  # nosec B102
        str(comp.compile(str(comp.encode(code)))),
        {"print": _print},
    )
    sys.stdout = sys.__stdout__
    out = code_out.getvalue()
    code_out.close()
    assert out == code


@pytest.fixture(params=range(25))
def code(int_size):
    return "".join(random.choice([chr(i) for i in range(int_size)]) for _ in range(25))


def test_conversions(compiler, code):
    run_conversion_test(compiler, code)


@pytest.fixture(params=range(11))
def number(request):
    if request.param == 0:
        return 0
    elif request.param < 6:
        return random.randint(1, 10000)
    else:
        return random.randint(1, 100) ** 2


def test_factor(number):
    a, b = bftools.factor(number)
    assert a * b == number


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


def test_hassizes():
    compiler = bftools.BrainfuckTools()
    assert compiler.array_size == 30000
    assert compiler.int_size == 8

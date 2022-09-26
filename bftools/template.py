# pylint: disable=invalid-name,global-statement
import sys

ARRAY_SIZE = int("{0}")
INT_SIZE = int("{1}")
data = bytearray(ARRAY_SIZE)
POSITION = 0


def _get_value() -> int:
    value = data[POSITION]
    for i in range(1, INT_SIZE // 8):
        value += data[POSITION + i] << (i * 8)
    return value


def _set_value(v: int) -> None:
    data[POSITION] = v & 0xFF
    for i in range(1, INT_SIZE // 8):
        data[POSITION + i] = (v >> (i * 8)) & 0xFF


def shift_right(a: int) -> None:
    """Shift the pointer right by the given amount."""
    global POSITION
    POSITION = (POSITION + a) % ARRAY_SIZE


def shift_left(a: int) -> None:
    """Shift the pointer left by the given amount."""
    shift_right(-a)


def increment(a: int) -> None:
    """Increment the value at the current position by the given amount."""
    _set_value((_get_value() + a) % (2**INT_SIZE))


def decrement(a: int) -> None:
    """Decrement the value at the current position by the given amount."""
    increment(-a)


def is_zero() -> bool:
    """Check if the value at the current position is zero."""
    return data[POSITION] == 0


def get_input() -> None:
    """Get input from the user."""
    data[POSITION] = ord(sys.stdin.read(1))


def output() -> None:
    """Output the value at the current position."""
    print(chr(_get_value()), end="")

import sys

array_size = int("{0}")
int_size = int("{1}")
data = bytearray(array_size)
position = 0


def _get_value() -> int:
    value = data[position]
    for i in range(1, int_size // 8):
        value += data[position + i] << (i * 8)
    return value


def _set_value(v: int) -> None:
    data[position] = v & 0xFF
    for i in range(1, int_size // 8):
        data[position + i] = (v >> (i * 8)) & 0xFF


def shift_right(a: int) -> None:
    """Shift the pointer right by the given amount."""
    global position
    position = (position + a) % array_size


def shift_left(a: int) -> None:
    """Shift the pointer left by the given amount."""
    shift_right(-a)


def increment(a: int) -> None:
    """Increment the value at the current position by the given amount."""
    _set_value((_get_value() + a) % (2**int_size))


def decrement(a: int) -> None:
    """Decrement the value at the current position by the given amount."""
    increment(-a)


def is_zero() -> bool:
    """Check if the value at the current position is zero."""
    return data[position] == 0


def get_input() -> None:
    """Get input from the user."""
    data[position] = ord(sys.stdin.read(1))


def output() -> None:
    """Output the value at the current position."""
    print(chr(_get_value()), end="")

from .base import BrainfuckBase, HasSizes, IntegerSize
from .tools import factor_optimized

__all__ = ("EncodedBrainfuck",)


class EncodedBrainfuck(BrainfuckBase, HasSizes):
    """An object to represent text encoded into Brainfuck.

    To receive the encoded Brainfuck, use :attr:`result` or
    str(:class:`EncodedBrainfuck`).

    .. warning::
        This class is not intended to be instantiated directly. Use :func:`encode_text` or :meth:`BrainfuckTools.encode`
        instead.

    Attributes
    ----------
    result: Optional[str]
        The result text. This will never be ``None`` unless :meth:`parse` has not been called. Since the library
        always calls :meth:`parse` before returning the object, this should never happen unless you override the
        functionality of the library.
    """

    def __init__(self, array_size: int = 30000, int_size: IntegerSize = 8) -> None:
        BrainfuckBase.__init__(self)
        HasSizes.__init__(self, array_size=array_size, int_size=int_size)

    def parse(self, value: str) -> None:
        """Parse the given text.

        .. note::
            You should not need to use this method. It is intended for internal use only, so you should only need to use
            it if you override the functionality of the library. This method is not dangerous like
            :meth:`DecodedBrainfuck.parse` is.

        .. note:
            The library currently does not use much optimization, but it will in the future. The
            current optimization simply factors the number into loops, so instead of "+++++++++++++++", it will become
            "+++[>+++++<-]". As the brainfuck code gets more advanced, this has room for even more optimization.
            Currently, it is planned to optimize the code further by recursively factoring the number into smaller
            numbers. For example, instead of factoring 10000 into ``100 * 100``, it will become
            ``(10 * 10) * (10 * 10)``. This is planned for v0.4.

        Parameters
        ----------
        value: str
            The text to parse.
        """
        # TODO: Optimize by factoring recursively
        self.result = ""
        for character in value:
            num = ord(character)
            added = 0
            # Use a walrus operator here when we drop support for Python 3.7
            factored = factor_optimized(num + added, 8)
            while len(factored) < 2:  # Does this cause an error for prime numbers?
                added += 1

            def to_bf(val: int) -> str:
                return ("+" if val > 0 else "-") * abs(val)

            self.result += (
                ">" * (len(factored) - 1)
                + to_bf(factored[0])
                + "".join(f"[<{to_bf(val)}" for i, val in enumerate(factored[1:]))
                + ">-]" * (len(factored) - 1)
                + "<" * (len(factored) - 1)
                + to_bf(-added)
                + ".>"
            )

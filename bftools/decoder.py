import io
import sys
from typing import Optional


class DecodedBrainfuck:
    def __init__(self):
        self._text: Optional[str] = None

    @property
    def text(self):
        return self._text

    def parse(self, code: str) -> None:
        code_out = io.StringIO()
        sys.stdout = code_out
        exec(code)
        sys.stdout = sys.__stdout__
        out = code_out.getvalue()
        code_out.close()
        self._text = out


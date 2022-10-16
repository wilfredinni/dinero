from typing import TypedDict


class Currency(TypedDict):
    code: str
    base: int
    exponent: int

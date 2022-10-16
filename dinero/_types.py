from typing import TypedDict
from typing_extensions import NotRequired


class Currency(TypedDict):
    code: str
    base: int
    exponent: int
    symbol: NotRequired[str]

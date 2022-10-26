from typing import TypedDict

from typing_extensions import NotRequired

OperationType = str | int | float


class Currency(TypedDict):
    code: str
    base: int
    exponent: int
    symbol: NotRequired[str]


class DineroDictionaryOutput(TypedDict):
    amount: str
    currency: Currency

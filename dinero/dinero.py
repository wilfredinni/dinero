from dataclasses import dataclass
from decimal import Decimal, getcontext

from ._types import Currency


class DifferentCurrencyError(Exception):
    """Operation could not be completed"""


@dataclass
class Dinero:
    amount: int | float | str
    currency: Currency

    @property
    def raw_amount(self):
        return self.amount

    @property
    def symbol(self):
        return self.currency.get("symbol", "$")

    @property
    def code(self):
        return self.currency.get("code")

    @property
    def exponent(self):
        return self.currency.get("exponent")

    @property
    def precision(self):
        return self.currency.get("base")

    @property
    def normalized_amount(self):
        return self.normalize(self.amount)

    def normalize(self, amount):
        getcontext().prec = self.precision
        return Decimal(amount).normalize()

    def add(self, amount: "str | int | float | Dinero") -> "Dinero":
        if isinstance(amount, Dinero):
            amount_to_add = amount
        else:
            amount_to_add = Dinero(str(amount), self.currency)

        if amount_to_add.code != self.code:
            raise DifferentCurrencyError("Currencies can not be different")

        result = self.normalized_amount + amount_to_add.normalized_amount
        return Dinero(result, self.currency)

    def formatted_amount(self, symbol: bool = False, currency: bool = False) -> str:
        currency_format = f",.{self.exponent}f"
        normalized_amount = self.normalized_amount

        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""
        return f"{currency_symbol}{normalized_amount:{currency_format}}{currency_code}"

    def __repr__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"Dinero({self.raw_amount} -> {formatted_output})"

    def __str__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"{formatted_output}"

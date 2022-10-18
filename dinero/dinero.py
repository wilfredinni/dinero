from dataclasses import dataclass
from ._types import Currency


@dataclass
class Dinero:
    amount: int | float
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
    def base(self):
        return self.currency.get("base")

    def formatted_amount(self, symbol: bool = False, currency: bool = False) -> str:
        currency_format = f",.{self.exponent}f"

        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""
        return f"{currency_symbol}{self.amount:{currency_format}}{currency_code}"

    def __repr__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"Dinero({self.raw_amount} -> {formatted_output})"

    def __str__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"{self.raw_amount} -> {formatted_output}"

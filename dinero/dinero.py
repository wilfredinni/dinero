from ._types import Currency


class Dinero:
    def __init__(self, amount: int | float, currency: Currency):
        self.amount = amount
        self.currency = currency

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
        currency_format = f",.{self.currency.get('exponent')}f"

        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""
        return f"{currency_symbol}{self.amount:{currency_format}}{currency_code}"

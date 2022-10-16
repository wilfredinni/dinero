from ._types import Currency


class Dinero:
    def __init__(self, amount: int | float, currency: Currency):
        self.amount = amount
        self.currency = currency

    @property
    def formatted_amount(self):
        currency_format = f",.{self.currency.get('exponent')}f"
        return f"{self.amount:{currency_format}}"

    @property
    def raw_amount(self):
        return self.amount

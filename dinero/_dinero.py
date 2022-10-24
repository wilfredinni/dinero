from dataclasses import dataclass
from decimal import Decimal, getcontext

from ._types import Currency, OperationType


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
        getcontext().prec = self.precision
        return Decimal(self.amount).normalize()

    def formatted_amount(self, symbol: bool = False, currency: bool = False) -> str:
        currency_format = f",.{self.exponent}f"
        normalized_amount = self.normalized_amount

        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""
        return f"{currency_symbol}{normalized_amount:{currency_format}}{currency_code}"

    def add(self, amount: "OperationType | Dinero") -> "Dinero":
        return self.__add__(amount)

    def subtract(self, amount: "OperationType | Dinero") -> "Dinero":
        return self.__sub__(amount)

    def multiply(self, amount: "OperationType | Dinero") -> "Dinero":
        return self.__mul__(amount)

    def divide(self, amount: "OperationType | Dinero") -> "Dinero":
        return self.__truediv__(amount)

    def equals_to(self, amount: "OperationType | Dinero") -> bool:
        return self.__eq__(amount)

    def _get_instance(self, amount: "OperationType | object | Dinero") -> "Dinero":
        if isinstance(amount, Dinero):
            second_amount = amount
        else:
            second_amount = Dinero(str(amount), self.currency)

        if second_amount.code != self.code:
            raise DifferentCurrencyError("Currencies can not be different")

        return second_amount

    def __add__(self, addend: "OperationType | Dinero") -> "Dinero":
        addend_obj = self._get_instance(addend)
        total = self.normalized_amount + addend_obj.normalized_amount
        return Dinero(str(total), self.currency)

    def __radd__(self, amount):
        if amount == 0:
            return self
        else:
            return self.__add__(amount)

    def __sub__(self, subtrahend: "OperationType | Dinero") -> "Dinero":
        subtrahend_obj = self._get_instance(subtrahend)
        total = self.normalized_amount - subtrahend_obj.normalized_amount
        return Dinero(str(total), self.currency)

    def __mul__(self, multiplicand: "OperationType | Dinero") -> "Dinero":
        multiplicand_obj = self._get_instance(multiplicand)
        total = self.normalized_amount * multiplicand_obj.normalized_amount
        return Dinero(str(total), self.currency)

    def __truediv__(self, divisor: "OperationType | Dinero") -> "Dinero":
        divisor_obj = self._get_instance(divisor)
        total = self.normalized_amount / divisor_obj.normalized_amount
        return Dinero(str(total), self.currency)

    def __eq__(self, amount: object) -> bool:
        if isinstance(amount, Dinero):
            if amount.code != self.code:
                return False

        amount_to_compare = self._get_instance(amount).normalized_amount
        amount = self.normalized_amount.quantize(amount_to_compare)
        return bool(amount == amount_to_compare)

    def __repr__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"Dinero({self.raw_amount} -> {formatted_output})"

    def __str__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"{formatted_output}"

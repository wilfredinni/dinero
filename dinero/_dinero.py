import json
from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import Any

from ._types import Currency, OperationType
from ._utils import amount_formatter, DecimalEncoder


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
    def normalized_amount(self) -> Decimal:
        places = Decimal(f"1e-{self.exponent}")
        getcontext().prec = self.precision
        return Decimal(self.amount).normalize().quantize(places)

    def formatted_amount(self, symbol: bool = False, currency: bool = False) -> str:
        formatted_amount = amount_formatter(self.normalized_amount, self.exponent)
        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""

        return f"{currency_symbol}{formatted_amount}{currency_code}"

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

    def less_than(self, amount: "OperationType | Dinero") -> bool:
        return self.__lt__(amount)

    def less_than_or_equal(self, amount: "OperationType | Dinero") -> bool:
        return self.__le__(amount)

    def greater_than(self, amount: "OperationType | Dinero") -> bool:
        return self.__gt__(amount)

    def greater_than_or_equal(self, amount: "OperationType | Dinero") -> bool:
        return self.__ge__(amount)

    def to_dict(self, amount_with_format: bool = False) -> dict[str, Any]:
        if amount_with_format:
            amount = amount_formatter(self.normalized_amount, self.exponent)
        else:
            amount = str(self.normalized_amount)

        _dict = self.__dict__
        _dict["amount"] = amount
        _dict["currency"].setdefault("symbol", "$")
        return _dict

    def to_json(self, amount_with_format: bool = False) -> str:
        dict_representation = self.to_dict(amount_with_format)
        return json.dumps(dict_representation, cls=DecimalEncoder)

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
        return self

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

        num_1 = self.normalized_amount
        num_2 = self._get_instance(amount).normalized_amount

        return bool(num_1 == num_2)

    def __lt__(self, amount: object) -> bool:
        num_1 = self.normalized_amount
        num_2 = self._get_instance(amount).normalized_amount
        return bool(num_1 < num_2)

    def __le__(self, amount: object) -> bool:
        num_1 = self.normalized_amount
        num_2 = self._get_instance(amount).normalized_amount
        return bool(num_1 <= num_2)

    def __gt__(self, amount: object) -> bool:
        num_1 = self.normalized_amount
        num_2 = self._get_instance(amount).normalized_amount
        return bool(num_1 > num_2)

    def __ge__(self, amount: object) -> bool:
        num_1 = self.normalized_amount
        num_2 = self._get_instance(amount).normalized_amount
        return bool(num_1 >= num_2)

    def __repr__(self):
        formatted_output = self.formatted_amount(symbol=True, currency=True)
        return f"Dinero({self.raw_amount} -> {formatted_output})"

    def __str__(self):
        formatted_output = self.formatted_amount()
        return f"{formatted_output}"

import json
from decimal import Decimal, getcontext
from typing import Any

from ._types import Currency, OperationType
from ._utils import DecimalEncoder
from .exceptions import DifferentCurrencyError, InvalidOperationError


class Base:
    def __init__(self, amount: int | float | str, currency: Currency):
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
    def precision(self):
        return self.currency.get("base")


class Utils(Base):
    def _get_instance(self, amount: "OperationType | object | Dinero") -> "Dinero":

        if not isinstance(amount, (int, float, str, Dinero)):
            msg = "You can only work against int, float, str and Dinero"
            raise InvalidOperationError(msg)

        if isinstance(amount, Dinero):
            amount_obj = amount
        else:
            amount_obj = Dinero(str(amount), self.currency)

        if amount_obj.code != self.code:
            raise DifferentCurrencyError("Currencies can not be different")

        return amount_obj

    def _normalize(self, quantize: bool = False) -> Decimal:
        places = Decimal(f"1e-{self.exponent}")
        getcontext().prec = self.precision
        normalized_amount = Decimal(self.amount).normalize()

        if quantize:
            return normalized_amount.quantize(places)

        return normalized_amount

    @property
    def _formatted_amount(self) -> str:
        currency_format = f",.{self.exponent}f"
        return f"{self._normalize(quantize=True):{currency_format}}"


class Operations(Utils):
    def __add__(self, addend: "OperationType | Dinero") -> "Dinero":
        addend_obj = self._get_instance(addend)
        total = self._normalize() + addend_obj._normalize()
        return Dinero(str(total), self.currency)

    def __radd__(self, obj):
        return self

    def __sub__(self, subtrahend: "OperationType | Dinero") -> "Dinero":
        subtrahend_obj = self._get_instance(subtrahend)
        total = self._normalize() - subtrahend_obj._normalize()
        return Dinero(str(total), self.currency)

    def __mul__(self, multiplicand: "OperationType | Dinero") -> "Dinero":
        multiplicand_obj = self._get_instance(multiplicand)
        total = self._normalize() * multiplicand_obj._normalize()
        return Dinero(str(total), self.currency)

    def __truediv__(self, divisor: "OperationType | Dinero") -> "Dinero":
        divisor_obj = self._get_instance(divisor)
        total = self._normalize() / divisor_obj._normalize()
        return Dinero(str(total), self.currency)

    def __eq__(self, amount: object) -> bool:
        if isinstance(amount, Dinero):
            if amount.code != self.code:
                return False

        num_2 = self._get_instance(amount)._normalize(quantize=True)
        num_1 = self._normalize(quantize=True)

        return bool(num_1 == num_2)

    def __lt__(self, amount: object) -> bool:
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 < num_2)

    def __le__(self, amount: object) -> bool:
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 <= num_2)

    def __gt__(self, amount: object) -> bool:
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 > num_2)

    def __ge__(self, amount: object) -> bool:
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 >= num_2)


class Dinero(Operations):
    def __init__(self, amount: int | float | str, currency: Currency):
        super().__init__(amount, currency)

    def get_amount(self, symbol: bool = False, currency: bool = False) -> str:
        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""
        return f"{currency_symbol}{self._formatted_amount}{currency_code}"

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
        normalized_amount = self._normalize(quantize=True)
        if amount_with_format:
            amount = self._formatted_amount
        else:
            amount = str(normalized_amount)

        _dict = self.__dict__
        _dict["amount"] = amount
        _dict["currency"].setdefault("symbol", "$")
        return _dict

    def to_json(self, amount_with_format: bool = False) -> str:
        dict_representation = self.to_dict(amount_with_format)
        return json.dumps(dict_representation, cls=DecimalEncoder)

    def __repr__(self):
        formatted_output = self.get_amount(symbol=True, currency=True)
        return f"Dinero({self.raw_amount} -> {formatted_output})"

    def __str__(self):
        formatted_output = self.get_amount()
        return f"{formatted_output}"

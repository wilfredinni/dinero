from decimal import Decimal
from typing import TYPE_CHECKING

from ._base import Base
from ._validators import Validators
from .types import Currency, OperationType

if TYPE_CHECKING:
    from ._dinero import Dinero


validate = Validators()


class Operations(Base):
    """All the operations supported between Dinero objects."""

    def __init__(self, amount: int | float | str, currency: Currency):
        super().__init__(amount, currency)

    def __add__(self, addend: "OperationType | Dinero") -> "Dinero":
        validate.addition_and_subtraction_amount(addend)
        addend_obj = self._get_instance(addend)
        total = self._normalize() + addend_obj._normalize()
        return self.__class__(str(total), self.currency)

    def __radd__(self, obj):
        return self

    def __sub__(self, subtrahend: "OperationType | Dinero") -> "Dinero":
        validate.addition_and_subtraction_amount(subtrahend)
        subtrahend_obj = self._get_instance(subtrahend)
        total = self._normalize() - subtrahend_obj._normalize()
        return self.__class__(str(total), self.currency)

    def __mul__(self, multiplicand: int | float | Decimal) -> "Dinero":
        validate.multiplication_and_division_amount(multiplicand)
        multiplicand_obj = self._get_instance(multiplicand)
        total = self._normalize() * multiplicand_obj._normalize()
        return self.__class__(str(total), self.currency)

    def __truediv__(self, divisor: int | float | Decimal) -> "Dinero":
        validate.multiplication_and_division_amount(divisor)
        divisor_obj = self._get_instance(divisor)
        total = self._normalize() / divisor_obj._normalize()
        return self.__class__(str(total), self.currency)

    def __eq__(self, amount: object) -> bool:
        validate.comparison_amount(amount)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        num_1 = self._normalize(quantize=True)
        return bool(num_1 == num_2)

    def __lt__(self, amount: object) -> bool:
        validate.comparison_amount(amount)
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 < num_2)

    def __le__(self, amount: object) -> bool:
        validate.comparison_amount(amount)
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 <= num_2)

    def __gt__(self, amount: object) -> bool:
        validate.comparison_amount(amount)
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 > num_2)

    def __ge__(self, amount: object) -> bool:
        validate.comparison_amount(amount)
        num_1 = self._normalize(quantize=True)
        num_2 = self._get_instance(amount)._normalize(quantize=True)
        return bool(num_1 >= num_2)

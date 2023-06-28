from decimal import Decimal, getcontext
from typing import TYPE_CHECKING

from ._validators import Validators
from .exceptions import DifferentCurrencyError
from .types import Currency, OperationType

if TYPE_CHECKING:
    from ._dinero import Dinero

validate = Validators()


class Base:
    """The base Dinero class with the constructor, properties and utils."""

    def __init__(self, amount: int | float | str | Decimal, currency: Currency):
        from ._dinero import Dinero

        self.amount = amount
        self.currency = currency
        self.dinero = Dinero

        validate.dinero_amount(amount)

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
    def _formatted_amount(self) -> str:
        currency_format = f",.{self.exponent}f"
        return f"{self._normalize(quantize=True):{currency_format}}"

    @property
    def raw_amount(self) -> Decimal:
        return self._normalize(quantize=True)

    def _get_instance(self, amount: "OperationType | Dinero") -> "Dinero":
        """Return a Dinero object after checking the currency codes are equal and
        transforming it to Dinero if needed.

        Args:
            amount (str, int, float, Decimal, Dinero): amount to be instantiated

        Returns:
            DINERO: Dinero object.
        """
        amount_obj = (
            amount
            if isinstance(amount, self.dinero)
            else self.dinero(amount, self.currency)
        )

        if amount_obj.code != self.code:
            raise DifferentCurrencyError("Currencies can not be different")

        return amount_obj

    def _normalize(self, quantize: bool = False) -> Decimal:
        """Return a Decimal object, that can be quantize.

        Args:
            quantize (bool): Only for the final result. Defaults to False.

        Returns
            DECIMAL: Decimal object.
        """

        getcontext().prec = self.precision
        normalized_amount = Decimal(self.amount).normalize()

        if quantize:
            places = Decimal(f"1e-{self.exponent}")
            normalized_amount = normalized_amount.quantize(places)

        return normalized_amount

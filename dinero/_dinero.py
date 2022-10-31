import json
from decimal import Decimal, InvalidOperation, getcontext
from typing import Any

from ._types import Currency, OperationType
from ._utils import DecimalEncoder
from .exceptions import DifferentCurrencyError, InvalidOperationError


class Base:
    """The base Dinero class with the constructor and properties."""

    def __init__(self, amount: int | float | str | Decimal, currency: Currency):
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
    """Utility class with the most important methods to count money exactly."""

    def _get_instance(self, amount: "OperationType | object | Dinero") -> "Dinero":
        """Return a Dinero object after checking the amount is of a valid type
        and transforming it to Dinero if needed.
        """

        if not isinstance(amount, (int, float, str, Decimal, Dinero)):
            raise InvalidOperationError(InvalidOperationError.message)

        if isinstance(amount, Dinero):
            amount_obj = amount
        else:
            amount_obj = Dinero(str(amount), self.currency)

        if amount_obj.code != self.code:
            raise DifferentCurrencyError("Currencies can not be different")

        return amount_obj

    def _normalize(self, quantize: bool = False) -> Decimal:
        try:
            getcontext().prec = self.precision

            if isinstance(self.amount, Dinero):
                normalized_amount = self.amount._normalize()
            else:
                normalized_amount = Decimal(self.amount).normalize()

            if quantize:
                places = Decimal(f"1e-{self.exponent}")
                normalized_amount = normalized_amount.quantize(places)

            return normalized_amount
        except (ValueError, InvalidOperation):
            raise InvalidOperationError(InvalidOperationError.message)

    @property
    def _formatted_amount(self) -> str:
        currency_format = f",.{self.exponent}f"
        return f"{self._normalize(quantize=True):{currency_format}}"


class Operations(Utils):
    """All the operations supported between Dinero objects."""

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
    """A Dinero object is an immutable data structure representing a specific monetary value.
    It comes with methods for creating, parsing, manipulating, testing and formatting them.

    Args:
        amount (str, int, float, Decimal)
        currency: (dict): Expressed as an ISO 4217 currency code.
    """

    def __init__(self, amount: int | float | str, currency: Currency):
        super().__init__(amount, currency)

    def format_amount(self, symbol: bool = False, currency: bool = False) -> str:
        """Format a Dinero object with his decimals, symbol and/or code.

        Example:
            >>> Dinero('12,34', USD).format(symbol=True, currency=True)

        Args:
            symbol (bool, optional): Add the country  currency symbol. Defaults to False.
            currency (bool, optional): Add the country currency code. Defaults to False.

        Returns:
            STR: Formatted string representation of a Dinero object.
        """
        currency_symbol = self.symbol if symbol else ""
        currency_code = f" {self.code}" if currency else ""
        return f"{currency_symbol}{self._formatted_amount}{currency_code}"

    def add(self, amount: "OperationType | Dinero") -> "Dinero":
        """Returns a new Dinero object that represents the sum of this and an other object.

        Example:
            >>> Dinero('12,34', USD).add(Dinero("1.4", USD))
            >>> Dinero('12,34', USD).add('1.4')
            >>> Dinero('12,34', USD).add(1.4)
            >>> Dinero('12,34', USD).add(14)

        Args:
            amount (str, int, float, Decimal, Dinero): The addend.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__add__(amount)

    def subtract(self, amount: "OperationType | Dinero") -> "Dinero":
        """
        Returns a new Dinero object that represents the difference of this and an other object.

        Example:
            >>> Dinero('12,34', USD).subtract(Dinero("1.4", USD))
            >>> Dinero('12,34', USD).subtract('1.4')
            >>> Dinero('12,34', USD).subtract(1.4)
            >>> Dinero('12,34', USD).subtract(14)

        Args:
            amount (str, int, float, Decimal, Dinero): The subtrahend.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__sub__(amount)

    def multiply(self, amount: "OperationType | Dinero") -> "Dinero":
        """
        Returns a new Dinero object that represents the multiplied value by the given factor.

        Example:
            >>> Dinero('12,34', USD).multiply(Dinero("2", USD))
            >>> Dinero('12,34', USD).multiply('2')
            >>> Dinero('12,34', USD).multiply(2.0)
            >>> Dinero('12,34', USD).multiply(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The multiplicand.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__mul__(amount)

    def divide(self, amount: "OperationType | Dinero") -> "Dinero":
        """Returns a new Dinero object that represents the divided value by the given factor.

        Example:
            >>> Dinero('12,34', USD).divide(Dinero("2", USD))
            >>> Dinero('12,34', USD).divide('2')
            >>> Dinero('12,34', USD).divide(2.0)
            >>> Dinero('12,34', USD).divide(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The divisor.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__truediv__(amount)

    def equals_to(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object equals to the other.

        Example:
            >>> Dinero('2,00', USD).equals_to(Dinero("2", USD))
            >>> Dinero('2,00', USD).equals_to('2')
            >>> Dinero('2,00', USD).equals_to(2.0)
            >>> Dinero('2,00', USD).equals_to(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__eq__(amount)

    def less_than(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object is less than the other.

        Example:
            >>> Dinero('2,00', USD).less_than(Dinero("2", USD))
            >>> Dinero('2,00', USD).less_than('2')
            >>> Dinero('2,00', USD).less_than(2.0)
            >>> Dinero('2,00', USD).less_than(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__lt__(amount)

    def less_than_or_equal(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object is less than or equal the other.

        Example:
            >>> Dinero('2,00', USD).less_than(Dinero("2", USD))
            >>> Dinero('2,00', USD).less_than('2')
            >>> Dinero('2,00', USD).less_than(2.0)
            >>> Dinero('2,00', USD).less_than(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__le__(amount)

    def greater_than(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object is greater or equal the other.

        Example:
            >>> Dinero('2,00', USD).greater_than(Dinero("2", USD))
            >>> Dinero('2,00', USD).greater_than('2')
            >>> Dinero('2,00', USD).greater_than(2.0)
            >>> Dinero('2,00', USD).greater_than(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__gt__(amount)

    def greater_than_or_equal(self, amount: "OperationType | Dinero") -> bool:
        """
        Checks whether the value represented by this object is greater than or equal the other.

        Example:
            >>> Dinero('2,00', USD).greater_than_or_equal(Dinero("2", USD))
            >>> Dinero('2,00', USD).greater_than_or_equal('2')
            >>> Dinero('2,00', USD).greater_than_or_equal(2.0)
            >>> Dinero('2,00', USD).greater_than_or_equal(2)

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dinero: Dinero object.
        """

        return self.__ge__(amount)

    def to_dict(self, amount_with_format: bool = False) -> dict[str, Any]:
        """Returns the object's data as a Python Dictionary.

        Example:
            >>> Dinero('2,00', USD).to_dict()
            >>> Dinero('2,00', USD).to_dict(amount_with_format=False)

        Args:
            amount_with_format (bool): If the amount is formatted or not. Defaults to False.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            Dict: The object's data as a Python Dictionary.
        """

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
        """Returns the object's data as a JSON string.

        Example:
            >>> Dinero('2,00', USD).to_json()
            >>> Dinero('2,00', USD).to_json(amount_with_format=False)

        Args:
            amount_with_format (bool): If the amount is formatted or not. Defaults to False.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        return:
            STR: The object's data as JSON.
        """

        dict_representation = self.to_dict(amount_with_format)
        return json.dumps(dict_representation, cls=DecimalEncoder)

    def __repr__(self):
        formatted_output = self.format_amount(symbol=True, currency=True)
        return f"Dinero({self.raw_amount} -> {formatted_output})"

    def __str__(self):
        formatted_output = self.format_amount()
        return f"{formatted_output}"

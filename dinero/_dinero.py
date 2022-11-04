"""This module allows the user to make exact monetary calculations.

The module contains the following functions:

- `format()` - Format a Dinero object with his decimals, symbol and/or code.
- `add()` - Returns a new Dinero object that represents the sum two amounts.
- `subtract()` - Returns a new Dinero object that represents the difference of two amounts.
- `multiply()` - Returns a new Dinero object that represents the multiplied value by a factor.
- `divide()` - Returns a new Dinero object that represents the divided value by a factor.
- `equals_to()` - Checks whether the value represented by this object equals to the other.
- `less_than()` - Checks whether the value represented by this object is less than the other.
- `less_than_or_equal()` - Checks whether an object is less than or equal the other.
- `greater_than()` - Checks whether an object is greater or equal the other.
- `greater_than_or_equal()` - Checks whether an object is greater or equal the other.
- `to_dict()` - Returns the object's data as a Python Dictionary.
- `to_json()` - Returns the object's data as a JSON string.
"""

import json
from decimal import Decimal, InvalidOperation, getcontext
from typing import Any

from .types import Currency, OperationType
from ._utils import DecimalEncoder
from .exceptions import DifferentCurrencyError, InvalidOperationError


class Base:
    """The base Dinero class with the constructor and properties."""

    def __init__(self, amount: int | float | str | Decimal, currency: Currency):
        self.amount = amount
        self.currency = currency

        _check_valid_amount(amount)

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
        """Return a Dinero object after checking the currency codes are equal and
        transforming it to Dinero if needed.

        Args:
            amount (str, int, float, Decimal, Dinero): amount to be instantiated

        Returns:
            DINERO: Dinero object.
        """

        if isinstance(amount, Dinero):
            amount_obj = amount
        else:
            amount_obj = Dinero(str(amount), self.currency)

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

        if isinstance(self.amount, Dinero):
            normalized_amount = self.amount._normalize()
        else:
            normalized_amount = Decimal(self.amount).normalize()

        if quantize:
            places = Decimal(f"1e-{self.exponent}")
            normalized_amount = normalized_amount.quantize(places)

        return normalized_amount

    @property
    def _formatted_amount(self) -> str:
        currency_format = f",.{self.exponent}f"
        return f"{self._normalize(quantize=True):{currency_format}}"

    @property
    def raw_amount(self) -> Decimal:
        return self._normalize(quantize=True)


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


class Dinero(Operations, Base):
    """A Dinero object is an immutable data structure representing a specific monetary value.
    It comes with methods for creating, parsing, manipulating, testing and formatting them.

    Args:
        amount (str, int, float, Decimal): The amount to work with.
        currency (dict): Expressed as an ISO 4217 currency code.
    """

    def __init__(self, amount: int | float | str, currency: Currency):
        super().__init__(amount, currency)

    def format(self, symbol: bool = False, currency: bool = False) -> str:
        """Format a Dinero object with his decimals, symbol and/or code.

        Examples:
            >>> Dinero('234342.3010', USD).format()
            234,342.30

            >>> Dinero('234342.3010', USD).format(symbol=True)
            $234,342.30

            >>> Dinero('234342.3010', USD).format(currency=True)
            234,342.30 USD

            >>> Dinero('234342.3010', USD).format(symbol=True, currency=True)
            $234,342.30 USD

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

        If the addend is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("2.32", USD)
            >>> amount_1.add(amount_2)
            4.64

            >>> amount = Dinero("2.32", USD)
            >>> amount.add("2.32")
            4.64

            >>> Dinero("2.32", USD) + Dinero("2.32", USD)
            4.64

            >>> Dinero("2.32", USD) + "2.32"
            4.64

        Args:
            amount (str, int, float, Decimal, Dinero): The addend.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DINERO: Dinero object.
        """

        return self.__add__(amount)

    def subtract(self, amount: "OperationType | Dinero") -> "Dinero":
        """
        Returns a new Dinero object that represents the difference of this and an other object.

        If the subtrahend is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("2", USD)
            >>> amount_1.subtract(amount_2)
            0.32

            >>> amount = Dinero("2.32", USD)
            >>> amount.subtract("2")
            0.32

            >>> Dinero("2.32", USD) - Dinero("2", USD)
            0.32

            >>> Dinero("2.32", USD) - "2"
            0.32

        Args:
            amount (str, int, float, Decimal, Dinero): The subtrahend.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DINERO: Dinero object.
        """

        return self.__sub__(amount)

    def multiply(self, amount: "OperationType | Dinero") -> "Dinero":
        """
        Returns a new Dinero object that represents the multiplied value by the given factor.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("3", USD)
            >>> amount_1.multiply(amount_2)
            6.96

            >>> amount = Dinero("2.32", USD)
            >>> amount.multiply("3")
            6.96

            >>> Dinero("2.32", USD) * Dinero("3", USD)
            6.96

            >>> Dinero("2.32", USD) * "3"
            6.96

        Args:
            amount (str, int, float, Decimal, Dinero): The multiplicand.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DINERO: Dinero object.
        """

        return self.__mul__(amount)

    def divide(self, amount: "OperationType | Dinero") -> "Dinero":
        """Returns a new Dinero object that represents the divided value by the given factor.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("3", USD)
            >>> amount_1.divide(amount_2)
            0.77

            >>> amount = Dinero("2.32", USD)
            >>> amount.divide("3")
            0.77

            >>> Dinero("2.32", USD) / Dinero("3", USD)
            0.77

            >>> Dinero("2.32", USD) / "3"
            0.77

        Args:
            amount (str, int, float, Decimal, Dinero): The divisor.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DINERO: Dinero object.
        """

        return self.__truediv__(amount)

    def equals_to(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object equals to the other.

        If the amount is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("2.32", USD)
            >>> amount_1.equals_to(amount_2)
            True

            >>> amount = Dinero("2.32", USD)
            >>> amount.equals_to("2.31")
            False

            >>> Dinero("2.32", USD) == Dinero("2.32", USD)
            True

            >>> Dinero("2.32", USD) == "2.31"
            False

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is equals to the other.
        """

        return self.__eq__(amount)

    def less_than(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object is less than the other.

        If the amount is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero(24, USD)
            >>> amount_2 = Dinero(25, USD)
            >>> amount_1.less_than(amount_2)
            True

            >>> amount = Dinero(24, USD)
            >>> amount.less_than("25")
            True

            >>> Dinero(24, USD) < Dinero(25, USD)
            True

            >>> Dinero(24, USD) < "25"
            True

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is less than to the other.
        """

        return self.__lt__(amount)

    def less_than_or_equal(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object is less than or equal the other.

        If the amount is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero(24, USD)
            >>> amount_2 = Dinero(25, USD)
            >>> amount_1.less_than_or_equal(amount_2)
            True

            >>> amount = Dinero(24, USD)
            >>> amount.less_than_or_equal("25")
            True

            >>> Dinero(24, USD) <= Dinero(25, USD)
            True

            >>> Dinero(24, USD) <= "25"
            True

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is less than or equal to the other.
        """

        return self.__le__(amount)

    def greater_than(self, amount: "OperationType | Dinero") -> bool:
        """Checks whether the value represented by this object is greater or equal the other.

        If the amount is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero(25, USD)
            >>> amount_2 = Dinero(24, USD)
            >>> amount_1.greater_than(amount_2)
            True

            >>> amount = Dinero(25, USD)
            >>> amount.greater_than("24")
            True

            >>> Dinero(25, USD) > Dinero(24, USD)
            True

            >>> Dinero(25, USD) > "24"
            True

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is greater than to the other.
        """

        return self.__gt__(amount)

    def greater_than_or_equal(self, amount: "OperationType | Dinero") -> bool:
        """
        Checks whether the value represented by this object is greater than or equal the other.

        If the amount is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero(25, USD)
            >>> amount_2 = Dinero(24, USD)
            >>> amount_1.greater_than_or_equal(amount_2)
            True

            >>> amount = Dinero(25, USD)
            >>> amount.greater_than_or_equal("24")
            True

            >>> Dinero(25, USD) >= Dinero(24, USD)
            True

            >>> Dinero(25, USD) >= "24"
            True

        Args:
            amount (str, int, float, Decimal, Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is greater than or equal to the other.
        """

        return self.__ge__(amount)

    def to_dict(self, amount_with_format: bool = False) -> dict[str, Any]:
        """Returns the object's data as a Python Dictionary.

        Examples:
            >>> Dinero("3333.259", USD).to_dict()
            {
                'amount': '3333.26',
                'currency':
                    {
                        'code': 'USD',
                        'base': 10,
                        'exponent': 2,
                        'symbol': '$'
                    }
            }

            >>> Dinero('3333.26', USD).to_dict(amount_with_format=True)
            {
                'amount': '3,333.26',
                'currency':
                    {
                        'code': 'USD',
                        'base': 10,
                        'exponent': 2,
                        'symbol': '$'
                    }
            }

        Args:
            amount_with_format (bool): If the amount is formatted or not. Defaults to False.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DICT: The object's data as a Python Dictionary.
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

        Examples:
            >>> Dinero('2,00', USD).to_json()
            '{"amount": "3333.20", "currency": {"code": "USD", "base": 10...'

            >>> Dinero('2,00', USD).to_json(amount_with_format=True)
            '{"amount": "3,333.26", "currency": {"code": "USD", "base": 10...'

        Args:
            amount_with_format (bool): If the amount is formatted or not. Defaults to False.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            STR: The object's data as JSON.
        """

        dict_representation = self.to_dict(amount_with_format)
        return json.dumps(dict_representation, cls=DecimalEncoder)

    def __repr__(self):
        return f"Dinero(amount={self.amount}, currency={self.currency})"

    def __str__(self):
        formatted_output = self.format()
        return f"{formatted_output}"


def _check_valid_amount(amount: int | float | str | Decimal) -> None:
    """Validate that the amount passed to Dinero is of valid type

    Args:
        amount (str, int, float, Decimal, Dinero)

    Raises:
        InvalidOperationError: An operation between unsupported types was executed.
    """
    try:
        if not isinstance(amount, (int, float, str, Decimal, Dinero)):
            raise InvalidOperationError(InvalidOperationError.message)

        Decimal(amount)

    except (ValueError, InvalidOperation):
        raise InvalidOperationError(InvalidOperationError.message)

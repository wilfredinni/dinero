"""
Dinero allows the user to make exact monetary calculations.

- format:: Format a Dinero object with his decimals, symbol and/or code.
- add:: Returns a new Dinero object that represents the sum two amounts.
- subtract:: Returns a new Dinero object that represents the difference of two amounts.
- multiply:: Returns a new Dinero object that represents the multiplied value by a factor.
- divide:: Returns a new Dinero object that represents the divided value by a factor.
- eq:: Checks whether the value represented by this object equals to the other.
- lt:: Checks whether the value represented by this object is less than the other.
- lte:: Checks whether an object is less than or equal the other.
- gt:: Checks whether an object is greater or equal the other.
- gte:: Checks whether an object is greater or equal the other.
- to_dict:: Returns the object's data as a Python Dictionary.
- to_json:: Returns the object's data as a JSON string.
- convert:: Converts the Dinero object to a different currency.
"""

import json
from decimal import Decimal
from typing import Any

from ._operations import Operations
from ._utils import DecimalEncoder
from ._validators import Validators
from .types import Currency, OperationType

validate = Validators()


class Dinero(Operations):
    """
    A Dinero object is an immutable data structure representing a specific
    monetary value. It comes with methods for creating, parsing, manipulating,
    testing and formatting them.

    Args:
        amount (str, int, float, Decimal): The amount to work with.
        currency (dict): Expressed as an ISO 4217 currency code.
    """

    def __init__(self, amount: int | float | str | Decimal, currency: Currency):
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
        """
        Returns a new Dinero object that represents the sum of this and an other object.

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
        Returns a new Dinero object that represents the difference of this and other.

        If the subtrahend is not a Dinero object, it will be transformed to one using the
        same currency.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("2", USD)
            >>> amount_1.subtract(amount_2)
            0.32

            >>> amount = Dinero("2.32", USD)
            >>> amount.subtract(2)
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

    def multiply(self, amount: int | float | Decimal) -> "Dinero":
        """
        Returns a new Dinero object that represents the multiplied value by
        the given factor.

        Examples:
            >>> amount = Dinero("2.32", USD)
            >>> amount.multiply(3)
            6.96

            >>> Dinero("2.32", USD) * 3
            6.96

        Args:
            amount (int, float, Decimal): The multiplicand.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DINERO: Dinero object.
        """

        return self.__mul__(amount)

    def divide(self, amount: int | float | Decimal) -> "Dinero":
        """
        Returns a new Dinero object that represents the divided value by the given factor.

        Examples:
            >>> amount = Dinero("2.32", USD)
            >>> amount.divide(3)
            0.77

            >>> Dinero("2.32", USD) / 3
            0.77

        Args:
            amount (int, float, Decimal): The divisor.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DINERO: Dinero object.
        """

        return self.__truediv__(amount)

    def eq(self, amount: "Dinero") -> bool:
        """
        Checks whether the value represented by this object equals to other instance.

        Examples:
            >>> amount_1 = Dinero("2.32", USD)
            >>> amount_2 = Dinero("2.32", USD)
            >>> amount_1.eq(amount_2)
            True

            >>> Dinero("2.32", USD) == Dinero("2.32", USD)
            True

        Args:
            amount (Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is equals to the other.
        """

        return self.__eq__(amount)

    def lt(self, amount: "Dinero") -> bool:
        """
        Checks whether the value represented by this object is less than the other.

        Examples:
            >>> amount_1 = Dinero(24, USD)
            >>> amount_2 = Dinero(25, USD)
            >>> amount_1.lt(amount_2)
            True

            >>> Dinero(24, USD) < Dinero(25, USD)
            True

        Args:
            amount (Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is less than to the other.
        """

        return self.__lt__(amount)

    def lte(self, amount: "Dinero") -> bool:
        """
        Checks whether the value represented by this object is less than or equal other.

        Examples:
            >>> amount_1 = Dinero(24, USD)
            >>> amount_2 = Dinero(25, USD)
            >>> amount_1.lte(amount_2)
            True

            >>> Dinero(24, USD) <= Dinero(25, USD)
            True

        Args:
            amount (Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is less than or equal to the other.
        """

        return self.__le__(amount)

    def gt(self, amount: "Dinero") -> bool:
        """
        Checks whether the value represented by this object is greater or equal other.

        Examples:
            >>> amount_1 = Dinero(25, USD)
            >>> amount_2 = Dinero(24, USD)
            >>> amount_1.gt(amount_2)
            True

            >>> Dinero(25, USD) > Dinero(24, USD)
            True

        Args:
            amount (Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is greater than to the other.
        """

        return self.__gt__(amount)

    def gte(self, amount: "Dinero") -> bool:
        """
        Checks whether the value represented by this object is greater than or equal other

        Examples:
            >>> amount_1 = Dinero(25, USD)
            >>> amount_2 = Dinero(24, USD)
            >>> amount_1.gte(amount_2)
            True

            >>> Dinero(25, USD) >= Dinero(24, USD)
            True

        Args:
            amount (Dinero): The object to compare to.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            BOOL: Whether the value represented is greater than or equal to the other.
        """

        return self.__ge__(amount)

    def to_dict(self, amount_with_format: bool = False) -> dict[str, Any]:
        """
        Returns the object's data as a Python Dictionary.

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
            amount_with_format (bool): If the amount is formatted. Defaults to False.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            DICT: The object's data as a Python Dictionary.
        """

        normalized_amount = self._normalize(quantize=True)
        amount = self._formatted_amount if amount_with_format else str(normalized_amount)

        dict_repr = self.__dict__
        dict_repr["amount"] = amount
        dict_repr["currency"].setdefault("symbol", "$")
        del dict_repr["dinero"]
        return dict_repr

    def to_json(self, amount_with_format: bool = False) -> str:
        """
        Returns the object's data as a JSON string.

        Examples:
            >>> Dinero('2,00', USD).to_json()
            '{"amount": "3333.20", "currency": {"code": "USD", "base": 10...'

            >>> Dinero('2,00', USD).to_json(amount_with_format=True)
            '{"amount": "3,333.26", "currency": {"code": "USD", "base": 10...'

        Args:
            amount_with_format (bool): If the amount is formatted. Defaults to False.

        Raises:
            DifferentCurrencyError: Different currencies where used.
            InvalidOperationError: An operation between unsupported types was executed.

        Returns:
            STR: The object's data as JSON.
        """

        dict_representation = self.to_dict(amount_with_format)
        return json.dumps(dict_representation, cls=DecimalEncoder)

    def convert(self, exchange_rate: str | float, currency: Currency) -> "Dinero":
        """
        Converts the Dinero object to a different currency using the specified
        exchange rate.

        Args:
            exchange_rate (str | float): The exchange rate to use for conversion.
            currency (Currency): The target currency to convert to.

        Returns:
            Dinero: A new Dinero object in the target currency.

        Raises:
            TypeError: If currency is not a Currency object.
            ValueError: If exchange_rate is negative, zero, or cannot be converted to
                a number.

        Examples:
            >>> from dinero.currencies import USD, EUR
            >>> usd_amount = Dinero("100", USD)
            >>> eur_amount = usd_amount.convert("0.85", EUR)
            >>> eur_amount.format()
            '85.00'

            >>> from dinero.currencies import CLP
            >>> clp_amount = usd_amount.convert(750, CLP)
            >>> clp_amount.format()
            '75,000'
        """
        from .tools.conversion import convert

        return convert(self, exchange_rate, currency)

    def __repr__(self):
        return f"Dinero(amount={self.amount}, currency={self.currency})"

    def __str__(self):
        formatted_output = self.format()
        return f"{formatted_output}"

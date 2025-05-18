"""
Currency Conversion Module

This module provides functionality to convert Dinero objects between different currencies
using specified exchange rates. It maintains the precision and immutability principles
of the Dinero library.

Key Features:
    - Convert Dinero objects to different currencies
    - Maintain proper decimal precision based on target currency
    - Support for all ISO 4217 currency formats
    - Precise calculations using Decimal type

Example:
    Converting USD to EUR with an exchange rate of 0.85:

    ```python
    from dinero import Dinero
    from dinero.currencies import USD, EUR

    # Create a USD amount
    usd_amount = Dinero("100", USD)

    # Convert to EUR
    eur_amount = usd_amount.convert("0.85", EUR)
    # Returns: Dinero("85.00", EUR)
    ```
"""

from decimal import Decimal, InvalidOperation

from dinero import Dinero
from dinero.types import Currency


def convert(dinero_obj: Dinero, exchange_rate: str | float, currency: Currency) -> Dinero:
    """
    Converts a Dinero object to a different currency using the specified exchange rate.

    Args:
        dinero_obj (Dinero): The Dinero object to convert.
        exchange_rate (str | float): The exchange rate to use for conversion.
        currency (Currency): The target currency to convert to.

    Returns:
        Dinero: A new Dinero object in the target currency.

    Raises:
        TypeError: If dinero_obj is not a Dinero object or currency is not a Currency obj.
        ValueError: If exchange_rate is negative, zero, or cannot be converted to an int.

    Examples:
        >>> from dinero import Dinero
        >>> from dinero.currencies import USD, EUR
        >>> usd_amount = Dinero("100", USD)
        >>> eur_amount = convert(usd_amount, "0.85", EUR)
        >>> eur_amount.format()
        '85.00'

        >>> from dinero.currencies import CLP
        >>> clp_amount = convert(usd_amount, 750, CLP)
        >>> clp_amount.format()
        '75,000'
    """
    # Validate the dinero_obj is a Dinero instance
    if not isinstance(dinero_obj, Dinero):
        raise TypeError("The first argument must be a Dinero object")

    # Validate the currency is a Currency dict
    if not isinstance(currency, dict) or not all(
        key in currency for key in ["code", "base", "exponent"]
    ):
        raise TypeError("The currency must be a valid Currency object")

    # Validate and convert the exchange rate
    try:
        decimal_rate = Decimal(str(exchange_rate))
    except (ValueError, InvalidOperation):
        raise ValueError("Exchange rate must be a valid number")

    # Ensure the exchange rate is positive
    if decimal_rate <= Decimal("0"):
        raise ValueError("Exchange rate must be a positive non-zero value")

    # Perform the conversion calculation
    source_amount = dinero_obj._normalize()
    target_amount = source_amount * decimal_rate

    # Create a new Dinero object in the target currency
    return Dinero(target_amount, currency)

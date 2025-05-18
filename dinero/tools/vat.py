"""
Value Added Tax (VAT) Module

VAT is a consumption tax applied to goods and services at each stage of production and
distribution. It is an indirect tax, meaning it is collected by businesses on behalf
of the tax authority and ultimately paid by the end consumer.

Key Concepts:
    - VAT is calculated as a percentage of the price of goods or services
    - It is included in the final price paid by consumers (gross amount)
    - Businesses can usually reclaim VAT on their purchases (input VAT)
    - The net amount is the price before VAT is added
    - The gross amount is the total price including VAT

Common Usage:
    - Retail pricing: Adding VAT to product prices
    - Business accounting: Calculating VAT for tax returns
    - Financial reporting: Separating net amounts from VAT portions

Example:
    For a product with a net price of $100 and a VAT rate of 20%:
    - Net amount: $100.00 (price before VAT)
    - VAT portion: $20.00 (20% of net amount)
    - Gross amount: $120.00 (total price including VAT)

This module provides tools for all these VAT-related calculations while maintaining
precise decimal arithmetic using the Dinero type system.
"""

from dinero import Dinero

from ._validators import ToolValidators


def calculate_net_amount(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Calculates the net amount (excluding VAT) from a gross amount (including VAT).

    Args:
        amount (Dinero): The gross amount (including VAT).
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The net amount (excluding VAT).

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number
        ValueError: If the vat_rate argument is negative

    Examples:
        >>> gross_amount = Dinero(120, USD)  # Amount including 20% VAT
        >>> net_amount = calculate_net_amount(gross_amount, 20)
        >>> net_amount.format(symbol=True, currency=True)
        '$100.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    divisor = 1 + (vat_rate / 100)
    return amount / divisor


def calculate_vat_portion(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Calculates the VAT portion from a gross amount (including VAT).

    Args:
        amount (Dinero): The gross amount (including VAT).
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The VAT portion.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number
        ValueError: If the vat_rate argument is negative

    Examples:
        >>> gross_amount = Dinero(120, USD)  # Amount including 20% VAT
        >>> vat = calculate_vat_portion(gross_amount, 20)
        >>> vat.format(symbol=True, currency=True)
        '$20.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    net_amount = calculate_net_amount(amount, vat_rate)
    return amount - net_amount


def calculate_gross_amount(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Calculates the gross amount (including VAT) from a net amount.

    Args:
        amount (Dinero): The net amount (excluding VAT).
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The gross amount (including VAT).

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number
        ValueError: If the vat_rate argument is negative

    Examples:
        >>> net_amount = Dinero(100, USD)  # Amount without VAT
        >>> gross_amount = calculate_gross_amount(net_amount, 20)
        >>> gross_amount.format(symbol=True, currency=True)
        '$120.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    vat_multiplier = 1 + (vat_rate / 100)
    return amount * vat_multiplier

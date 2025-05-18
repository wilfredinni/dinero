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

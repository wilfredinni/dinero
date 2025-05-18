from dinero import Dinero

from ._validators import ToolValidators


def extract_amount_without_vat(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Extracts the amount without VAT from a total amount that includes VAT.

    Args:
        amount (Dinero): The amount including VAT.
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The amount without VAT.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number
        ValueError: If the vat_rate argument is negative

    Examples:
        >>> total = Dinero(120, USD)  # Amount including 20% VAT
        >>> amount = extract_amount_without_vat(total, 20)
        >>> amount.format(symbol=True, currency=True)
        '$100.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    divisor = 1 + (vat_rate / 100)
    return amount / divisor


def extract_vat_amount(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Extracts the VAT amount from a total that includes VAT.

    Args:
        amount (Dinero): The amount including VAT.
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The VAT amount.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number
        ValueError: If the vat_rate argument is negative

    Examples:
        >>> total = Dinero(120, USD)  # Amount including 20% VAT
        >>> vat = extract_vat_amount(total, 20)
        >>> vat.format(symbol=True, currency=True)
        '$20.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    amount_without_vat = extract_amount_without_vat(amount, vat_rate)
    return amount - amount_without_vat


def add_vat(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Adds VAT to an amount that does not include VAT.

    Args:
        amount (Dinero): The amount without VAT.
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The amount including VAT.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number
        ValueError: If the vat_rate argument is negative

    Examples:
        >>> net_amount = Dinero(100, USD)  # Amount without VAT
        >>> total = add_vat(net_amount, 20)
        >>> total.format(symbol=True, currency=True)
        '$120.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    vat_multiplier = 1 + (vat_rate / 100)
    return amount * vat_multiplier

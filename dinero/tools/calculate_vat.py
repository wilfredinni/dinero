from dinero import Dinero
from dinero.exceptions import InvalidOperationError


def calculate_vat(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Calculates the VAT amount for a given Dinero object.

    Args:
        amount (Dinero): The amount to calculate the VAT for.
        vat_rate (int | float): The VAT rate as a percentage.

    Returns:
        Dinero: The VAT amount.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the vat_rate argument is not a number.
        ValueError: If the vat_rate argument is negative.

    Examples:
        >>> amount = Dinero(100, USD)
        >>> vat_amount = calculate_vat(amount, 7.25)
        >>> vat_amount.format(symbol=True, currency=True)
        '$6.76 USD'
    """
    if not isinstance(amount, Dinero):
        raise InvalidOperationError(InvalidOperationError.operation_msg)

    if not isinstance(vat_rate, (int, float)):
        raise TypeError("The vat_rate argument must be a number.")

    if vat_rate < 0:
        raise ValueError("The vat_rate argument cannot be negative.")

    divisor = 1 + (vat_rate / 100)
    amount_without_vat = amount / divisor
    vat_amount = amount - amount_without_vat
    return vat_amount

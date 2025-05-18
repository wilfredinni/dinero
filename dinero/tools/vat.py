from dinero import Dinero

from ._validators import ToolValidators


def extract_vat(amount: Dinero, vat_rate: int | float) -> Dinero:
    """
    Calculates the VAT amount of a given Dinero object.

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
        >>> vat_amount = extract_vat(amount, 7.25)
        >>> vat_amount.format(symbol=True, currency=True)
        '$6.76 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, vat_rate)
    divisor = 1 + (vat_rate / 100)
    amount_without_vat = amount / divisor
    vat_amount = amount - amount_without_vat
    return vat_amount

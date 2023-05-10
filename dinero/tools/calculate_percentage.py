from dinero import Dinero
from dinero.exceptions import InvalidOperationError


def calculate_percentage(amount: Dinero, percentage: int | float) -> Dinero:
    """
    Calculates the percentage of a given Dinero object.

    Args:
        amount (Dinero): The amount to calculate the percentage of.
        percentage (int | float): The percentage to calculate.

    Returns:
        Dinero: The calculated percentage of the amount.

    Raises:
        InvalidOperationError: If the amount is not an instance of Dinero.
        TypeError: If the percentage argument is not a number.
        ValueError: If the percentage argument is negative.

    Example:
        >>> amount = Dinero("3000", CLP)
        >>> percentage_amount = calculate_percentage(amount, 15)
        >>> percentage_amount.format(symbol=True, currency=True)
        '$450.00 USD'
    """
    if not isinstance(amount, Dinero):
        raise InvalidOperationError(InvalidOperationError.operation_msg)

    if not isinstance(percentage, (int, float)):
        raise TypeError("The percentage argument must be a number.")

    if percentage < 0:
        raise ValueError("The percentage argument cannot be negative.")

    return amount * (percentage / 100)

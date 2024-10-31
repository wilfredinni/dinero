from dinero import Dinero

from ._validators import ToolValidators
from .calculate_percentage import calculate_percentage


def calculate_markup(cost: Dinero, markup: int | float) -> Dinero:
    """
    Calculates the markup of a given Dinero object.

    Args:
        cost (Dinero): The cost to calculate the markup of.
        markup (int | float): The markup to calculate.

    Returns:
        Dinero: The calculated markup of the cost.

    Raises:
        InvalidOperationError: If the cost is not an instance of Dinero.
        TypeError: If the markup argument is not a number.
        ValueError: If the markup argument is negative.

    Examples:
        >>> cost = Dinero("3000", USD)
        >>> markup_amount = calculate_markup(cost, 15)
        >>> markup_amount.format(symbol=True, currency=True)
        '$3,450.00 USD'
    """
    validate = ToolValidators()
    validate.percentage_inputs(cost, markup)
    markup_amount = calculate_percentage(cost, markup)
    final_amount = cost + markup_amount
    return final_amount

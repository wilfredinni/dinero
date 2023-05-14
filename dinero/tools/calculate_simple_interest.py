from dinero import Dinero
from dinero.exceptions import InvalidOperationError


def calculate_simple_interest(
    principal: Dinero, interest_rate: int | float, duration: int
) -> Dinero:
    """
    Calculates the simple interest on a loan given the principal, interest rate, and duration.
    Calculate the total interest using the formula: I = P * r * t

    Args:
        principal (Dinero): The principal amount of the loan.
        interest_rate (float): The annual interest rate.
        duration (int): The duration of the loan in years.

    Raises:
        InvalidOperationError: If the principal amount is not a Dinero object.
        TypeError: If the interest rate is not a number or the duration is not an integer.
        ValueError: If the interest rate or duration is negative.

    Returns:
        Dinero: The total interest on the loan.

    Examples:
        >>> principal = Dinero(1000, USD)
        >>> interest_rate = 5
        >>> duration = 2
        >>> calculate_simple_interest(principal, interest_rate, duration)
        Dinero(100)
    """
    validate_inputs(principal, interest_rate, duration)

    # Calculate the total interest using the formula: I = P * r * t
    return principal * (interest_rate / 100) * duration


def validate_inputs(
    principal: Dinero, interest_rate: int | float, duration: int
) -> None:
    if not isinstance(principal, Dinero):
        raise InvalidOperationError(InvalidOperationError.operation_msg)

    if not isinstance(interest_rate, (int, float)):
        raise TypeError("The interest rate must be a number.")

    if not isinstance(duration, int):
        raise TypeError("The duration must be an integer.")

    if interest_rate < 0:
        raise ValueError("The interest rate cannot be negative.")

    if duration < 0:
        raise ValueError("The duration cannot be negative.")

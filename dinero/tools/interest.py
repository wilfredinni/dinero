"""
Interest calculation tools for working with monetary values.

This module provides tools for calculating both simple and compound interest
on monetary amounts. It handles all calculations using the Dinero class to
ensure precision in financial computations.

Simple interest is calculated using the formula:
    I = P * r * t
    where:
    - I is the interest earned
    - P is the principal amount
    - r is the annual interest rate (as a percentage)
    - t is the time in years

Compound interest is calculated using the formula:
    A = P * (1 + r/n)^(n*t)
    Interest = A - P
    where:
    - A is the final amount
    - P is the principal amount
    - r is the annual interest rate (as a decimal)
    - n is the number of times interest is compounded per year
    - t is the time in years

All monetary values are handled as Dinero instances to maintain precision
and proper decimal handling as per currency specifications.
"""

from dinero import Dinero

from ._validators import ToolValidators


def calculate_simple_interest(
    principal: Dinero, interest_rate: int | float, duration: int
) -> Dinero:
    """
    Calculates the simple interest on a loan given the principal, interest
    rate, and duration.
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
    validate = ToolValidators()
    validate.simple_interest_inputs(principal, interest_rate, duration)

    # Calculate the total interest using the formula: I = P * r * t
    return principal * (interest_rate / 100) * duration


def calculate_compound_interest(
    principal: Dinero, interest_rate: float, duration: int, compound_frequency: int
) -> Dinero:
    """
    Calculates the compound interest on a loan given the principal, interest rate,
    duration, and compound frequency. Uses the formula A = P * (1 + r/n)^(n*t)

    Args:
        principal (Dinero): The principal amount of the loan.
        interest_rate (float): The annual interest rate as a decimal.
        duration (int): The duration of the loan in years.
        compound_frequency (int): The number of times interest is compounded per year.

    Returns:
        Dinero: The total interest on the loan.

    Raises:
        InvalidOperationError: If the principal is not a Dinero object.
        ValueError: If the interest, duration, or frequency are not positive integers.

    Examples:
        >>> principal = Dinero(1000, USD)
        >>> interest_rate = 5.0
        >>> duration = 10
        >>> compound_frequency = 12
        >>> calculate_compound_interest(principal, interest_rate, duration, compound_frequency)  # noqa
        Dinero(648.34)
    """
    validate = ToolValidators()
    validate.compound_interest_inputs(
        principal, interest_rate, duration, compound_frequency
    )

    # Calculate using compound interest formula:
    # Total amount (A) = P * (1 + r/n)^(n*t)
    # Interest = A - P
    n = compound_frequency
    r = interest_rate / 100
    t = duration

    total_amount = principal * ((1 + r / n) ** (n * t))
    return total_amount - principal

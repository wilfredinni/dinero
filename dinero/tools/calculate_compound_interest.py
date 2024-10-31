from dinero import Dinero

from ._validators import ToolValidators


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

    # Calculate the total interest using the formula: A = P * (1 + r/n)^(n*t)
    n = compound_frequency
    r = interest_rate / 100
    t = duration
    return principal * ((1 + r / n) ** (n * t) - 1)

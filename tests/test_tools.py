import pytest

from dinero import Dinero
from dinero.currencies import EUR, JPY, USD
from dinero.exceptions import InvalidOperationError
from dinero.tools import (
    calculate_compound_interest,
    calculate_percentage,
    calculate_simple_interest,
)


@pytest.mark.parametrize(
    "amount, percentage, expected_result",
    [
        (Dinero("3000", USD), 15, Dinero("450", USD)),
        (Dinero("3000", USD), 0, Dinero("0", USD)),
        (Dinero("3000", USD), 100, Dinero("3000", USD)),
        (Dinero("3000", EUR), 15, Dinero("450", EUR)),
        (Dinero("3000", EUR), 0, Dinero("0", EUR)),
        (Dinero("3000", EUR), 100, Dinero("3000", EUR)),
        (Dinero("3000", USD), "15", TypeError),
        (Dinero("3000", USD), -15, ValueError),
        (3000, 15, InvalidOperationError),
    ],
)
def test_calculate_percentage(amount, percentage, expected_result):
    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            calculate_percentage(amount, percentage)
    else:
        percentage = calculate_percentage(amount, percentage)
        assert percentage == expected_result


@pytest.mark.parametrize(
    "principal, interest_rate, duration, expected_interest, error",
    [
        (Dinero(1000, USD), 5, 2, Dinero(100, USD), None),
        (Dinero(500, EUR), 3.5, 3, Dinero(52.5, EUR), None),
        (1000, 5, 2, None, InvalidOperationError),
        (Dinero(1000, USD), 5, "2.5", None, TypeError),
        (Dinero(1000, USD), 5, 2.5, None, TypeError),
        (Dinero(1000, USD), -5, 2, None, ValueError),
        (Dinero(1000, USD), 5, -2, None, ValueError),
    ],
)
def test_calculate_simple_interest(
    principal, interest_rate, duration, expected_interest, error
):
    if error:
        with pytest.raises(error):
            calculate_simple_interest(
                principal=principal,
                interest_rate=interest_rate,
                duration=duration,
            )
    else:
        interest = calculate_simple_interest(
            principal=principal,
            interest_rate=interest_rate,
            duration=duration,
        )
        assert interest == expected_interest


@pytest.mark.parametrize(
    "principal, interest_rate, duration, compound_frequency, expected, error",
    [
        (Dinero(1000, USD), 5.0, 10, 12, Dinero(647.01, USD), None),
        (Dinero(500, EUR), 2.5, 5, 4, Dinero(66.35, EUR), None),
        (Dinero(2000, JPY), 1.0, 3, 1, Dinero(60.60, JPY), None),
        (1000, 5.0, 10, 12, None, InvalidOperationError),
        (Dinero(1000, USD), -5.0, 10, 12, None, ValueError),
        (Dinero(1000, USD), 5.0, -10, 12, None, ValueError),
        (Dinero(1000, USD), 5.0, 10, -12, None, ValueError),
    ],
)
def test_calculate_compound_interest(
    principal, interest_rate, duration, compound_frequency, expected, error
):
    if error:
        with pytest.raises(error):
            calculate_compound_interest(
                principal=principal,
                interest_rate=interest_rate,
                duration=duration,
                compound_frequency=compound_frequency,
            )
    else:
        compound_interest = calculate_compound_interest(
            principal=principal,
            interest_rate=interest_rate,
            duration=duration,
            compound_frequency=compound_frequency,
        )
        assert compound_interest.equals_to(expected)

import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR, CLP
from dinero.exceptions import InvalidOperationError
from dinero.tools import calculate_vat, calculate_percentage, calculate_simple_interest


@pytest.mark.parametrize(
    "amount, vat_rate, expected_vat_amount",
    [
        (Dinero(100, USD), 7.25, Dinero("6.76", USD)),
        (Dinero(50, EUR), 21, Dinero("8.68", EUR)),
        (Dinero(500, CLP), 19, Dinero("80", CLP)),
        (100, 7.25, InvalidOperationError),
        (Dinero(100, USD), "7.25", TypeError),
        (Dinero(100, USD), -7.25, ValueError),
    ],
)
def test_calculate_vat(amount, vat_rate, expected_vat_amount):
    if isinstance(expected_vat_amount, type) and issubclass(
        expected_vat_amount, Exception
    ):
        with pytest.raises(expected_vat_amount):
            calculate_vat(amount, vat_rate)
    else:
        assert calculate_vat(amount, vat_rate) == expected_vat_amount


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
        assert calculate_percentage(amount, percentage) == expected_result


@pytest.mark.parametrize(
    "principal, interest_rate, duration, expected_interest",
    [
        (Dinero(1000, USD), 5, 2, Dinero(100, USD)),
        (Dinero(500, EUR), 3.5, 3, Dinero(52.5, EUR)),
    ],
)
def test_calculate_simple_interest(
    principal, interest_rate, duration, expected_interest
):
    assert (
        calculate_simple_interest(principal, interest_rate, duration)
        == expected_interest
    )

    # Test invalid input
    with pytest.raises(InvalidOperationError):
        calculate_simple_interest(1000, interest_rate, duration)  # type: ignore

    with pytest.raises(TypeError):
        calculate_simple_interest(principal, "5", duration)  # type: ignore

    with pytest.raises(TypeError):
        calculate_simple_interest(principal, interest_rate, 2.5)  # type: ignore

    with pytest.raises(ValueError):
        calculate_simple_interest(principal, -5, duration)

    with pytest.raises(ValueError):
        calculate_simple_interest(principal, interest_rate, -2)

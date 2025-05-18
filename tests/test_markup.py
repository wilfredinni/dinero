import pytest

from dinero import Dinero
from dinero.currencies import CLP, EUR, USD
from dinero.exceptions import InvalidOperationError
from dinero.tools.markup import (
    calculate_base_amount,
    calculate_marked_up_amount,
    calculate_markup_portion,
)


@pytest.mark.parametrize(
    "amount, markup_rate, expected_amount",
    [
        # Standard cases
        (Dinero(115, USD), 15, Dinero(100, USD)),  # 15% markup
        (Dinero(150, EUR), 50, Dinero(100, EUR)),  # 50% markup
        (Dinero(119, CLP), 19, Dinero(100, CLP)),  # 19% markup
        # Error cases
        (100, 15, InvalidOperationError),  # Invalid amount type
        (Dinero(100, USD), "15", TypeError),  # Invalid markup rate type
        (Dinero(100, USD), -15, ValueError),  # Negative markup rate
    ],
)
def test_calculate_base_amount(amount, markup_rate, expected_amount):
    """Test extracting base amount from final amount including markup"""
    if isinstance(expected_amount, type) and issubclass(expected_amount, Exception):
        with pytest.raises(expected_amount):
            calculate_base_amount(amount, markup_rate)
    else:
        result = calculate_base_amount(amount, markup_rate)
        assert result == expected_amount


@pytest.mark.parametrize(
    "amount, markup_rate, expected_markup",
    [
        # Standard cases
        (Dinero(115, USD), 15, Dinero(15, USD)),  # 15% markup
        (Dinero(150, EUR), 50, Dinero(50, EUR)),  # 50% markup
        (Dinero(119, CLP), 19, Dinero(19, CLP)),  # 19% markup
        # Error cases
        (100, 15, InvalidOperationError),  # Invalid amount type
        (Dinero(100, USD), "15", TypeError),  # Invalid markup rate type
        (Dinero(100, USD), -15, ValueError),  # Negative markup rate
    ],
)
def test_calculate_markup_portion(amount, markup_rate, expected_markup):
    """Test extracting markup portion from final amount"""
    if isinstance(expected_markup, type) and issubclass(expected_markup, Exception):
        with pytest.raises(expected_markup):
            calculate_markup_portion(amount, markup_rate)
    else:
        result = calculate_markup_portion(amount, markup_rate)
        assert result == expected_markup


@pytest.mark.parametrize(
    "amount, markup_rate, expected_total",
    [
        # Standard cases
        (Dinero(100, USD), 15, Dinero(115, USD)),  # 15% markup
        (Dinero(100, EUR), 50, Dinero(150, EUR)),  # 50% markup
        (Dinero(100, CLP), 19, Dinero(119, CLP)),  # 19% markup
        # Error cases
        (100, 15, InvalidOperationError),  # Invalid amount type
        (Dinero(100, USD), "15", TypeError),  # Invalid markup rate type
        (Dinero(100, USD), -15, ValueError),  # Negative markup rate
    ],
)
def test_calculate_marked_up_amount(amount, markup_rate, expected_total):
    """Test adding markup to base amount"""
    if isinstance(expected_total, type) and issubclass(expected_total, Exception):
        with pytest.raises(expected_total):
            calculate_marked_up_amount(amount, markup_rate)
    else:
        result = calculate_marked_up_amount(amount, markup_rate)
        assert result == expected_total


@pytest.mark.parametrize(
    "amount, markup_rate",
    [
        (Dinero(115, USD), 15),  # 15% markup
        (Dinero(150, EUR), 50),  # 50% markup
        (Dinero(119, CLP), 19),  # 19% markup
    ],
)
def test_markup_functions_consistency(amount, markup_rate):
    """Test that markup functions are mathematically consistent with each other"""
    # Extract base amount and markup from final amount
    base_amount = calculate_base_amount(amount, markup_rate)
    markup_amount = calculate_markup_portion(amount, markup_rate)

    # Verify that base + markup = final
    assert base_amount + markup_amount == amount

    # Verify that marking up base gives final
    assert calculate_marked_up_amount(base_amount, markup_rate) == amount

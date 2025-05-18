import pytest

from dinero import Dinero
from dinero.currencies import CLP, EUR, USD
from dinero.exceptions import InvalidOperationError
from dinero.tools.vat import (
    calculate_gross_amount,
    calculate_net_amount,
    calculate_vat_portion,
)


@pytest.mark.parametrize(
    "amount, vat_rate, expected_amount",
    [
        # Standard cases
        (Dinero(120, USD), 20, Dinero(100, USD)),  # 20% VAT
        (Dinero(50, EUR), 10, Dinero("45.45", EUR)),  # 10% VAT
        (Dinero(119, CLP), 19, Dinero(100, CLP)),  # 19% VAT
        # Error cases
        (100, 20, InvalidOperationError),  # Invalid amount type
        (Dinero(100, USD), "20", TypeError),  # Invalid VAT rate type
        (Dinero(100, USD), -20, ValueError),  # Negative VAT rate
    ],
)
def test_calculate_net_amount(amount, vat_rate, expected_amount):
    """Test extracting net amount from gross amount including VAT"""
    if isinstance(expected_amount, type) and issubclass(expected_amount, Exception):
        with pytest.raises(expected_amount):
            calculate_net_amount(amount, vat_rate)
    else:
        result = calculate_net_amount(amount, vat_rate)
        assert result == expected_amount


@pytest.mark.parametrize(
    "amount, vat_rate, expected_vat",
    [
        # Standard cases
        (Dinero(120, USD), 20, Dinero(20, USD)),  # 20% VAT
        (Dinero(50, EUR), 10, Dinero("4.55", EUR)),  # 10% VAT
        (Dinero(119, CLP), 19, Dinero(19, CLP)),  # 19% VAT
        # Error cases
        (100, 20, InvalidOperationError),  # Invalid amount type
        (Dinero(100, USD), "20", TypeError),  # Invalid VAT rate type
        (Dinero(100, USD), -20, ValueError),  # Negative VAT rate
    ],
)
def test_calculate_vat_portion(amount, vat_rate, expected_vat):
    """Test extracting VAT amount from gross amount"""
    if isinstance(expected_vat, type) and issubclass(expected_vat, Exception):
        with pytest.raises(expected_vat):
            calculate_vat_portion(amount, vat_rate)
    else:
        result = calculate_vat_portion(amount, vat_rate)
        assert result == expected_vat


@pytest.mark.parametrize(
    "amount, vat_rate, expected_total",
    [
        # Standard cases
        (Dinero(100, USD), 20, Dinero(120, USD)),  # 20% VAT
        (Dinero("45.45", EUR), 10, Dinero(50, EUR)),  # 10% VAT
        (Dinero(100, CLP), 19, Dinero(119, CLP)),  # 19% VAT
        # Error cases
        (100, 20, InvalidOperationError),  # Invalid amount type
        (Dinero(100, USD), "20", TypeError),  # Invalid VAT rate type
        (Dinero(100, USD), -20, ValueError),  # Negative VAT rate
    ],
)
def test_calculate_gross_amount(amount, vat_rate, expected_total):
    """Test adding VAT to net amount"""
    if isinstance(expected_total, type) and issubclass(expected_total, Exception):
        with pytest.raises(expected_total):
            calculate_gross_amount(amount, vat_rate)
    else:
        result = calculate_gross_amount(amount, vat_rate)
        assert result == expected_total


@pytest.mark.parametrize(
    "amount, vat_rate",
    [
        (Dinero(120, USD), 20),  # 20% VAT
        (Dinero(50, EUR), 10),  # 10% VAT
        (Dinero(119, CLP), 19),  # 19% VAT
    ],
)
def test_vat_functions_consistency(amount, vat_rate):
    """Test that VAT functions are mathematically consistent with each other"""
    # Extract net amount and VAT from gross amount
    net_amount = calculate_net_amount(amount, vat_rate)
    vat_amount = calculate_vat_portion(amount, vat_rate)

    # Verify that net + VAT = gross
    assert net_amount + vat_amount == amount

    # Verify that adding VAT to net gives original gross
    assert calculate_gross_amount(net_amount, vat_rate) == amount

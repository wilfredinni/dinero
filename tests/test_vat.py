import pytest

from dinero import Dinero
from dinero.currencies import CLP, EUR, USD
from dinero.exceptions import InvalidOperationError
from dinero.tools.vat import add_vat, extract_amount_without_vat, extract_vat_amount


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
def test_extract_amount_without_vat(amount, vat_rate, expected_amount):
    if isinstance(expected_amount, type) and issubclass(expected_amount, Exception):
        with pytest.raises(expected_amount):
            extract_amount_without_vat(amount, vat_rate)
    else:
        result = extract_amount_without_vat(amount, vat_rate)
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
def test_extract_vat_amount(amount, vat_rate, expected_vat):
    if isinstance(expected_vat, type) and issubclass(expected_vat, Exception):
        with pytest.raises(expected_vat):
            extract_vat_amount(amount, vat_rate)
    else:
        result = extract_vat_amount(amount, vat_rate)
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
def test_add_vat(amount, vat_rate, expected_total):
    if isinstance(expected_total, type) and issubclass(expected_total, Exception):
        with pytest.raises(expected_total):
            add_vat(amount, vat_rate)
    else:
        result = add_vat(amount, vat_rate)
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
    net_amount = extract_amount_without_vat(amount, vat_rate)
    vat_amount = extract_vat_amount(amount, vat_rate)

    # Verify that net + VAT = gross
    assert net_amount + vat_amount == amount

    # Verify that adding VAT to net gives gross
    assert add_vat(net_amount, vat_rate) == amount

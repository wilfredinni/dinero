import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR, CLP
from dinero.exceptions import InvalidOperationError
from dinero.tools import calculate_vat


@pytest.mark.parametrize(
    "amount, vat_rate, expected_vat_amount",
    [
        (Dinero(100, USD), 7.25, Dinero("6.76", USD)),
        (Dinero(50, EUR), 21, Dinero("8.68", EUR)),
        (Dinero(500, CLP), 19, Dinero("80", CLP)),
    ],
)
def test_calculate_vat(amount, vat_rate, expected_vat_amount):
    assert calculate_vat(amount, vat_rate) == expected_vat_amount


def test_calculate_vat_invalid_amount():
    amount = 100
    vat_rate = 7.25

    with pytest.raises(InvalidOperationError):
        calculate_vat(amount, vat_rate)  # type: ignore


def test_calculate_vat_invalid_vat_rate():
    amount = Dinero(100, USD)
    vat_rate = "7.25"

    with pytest.raises(TypeError):
        calculate_vat(amount, vat_rate)  # type: ignore


def test_calculate_vat_negative_vat_rate():
    amount = Dinero(100, USD)
    vat_rate = -7.25

    with pytest.raises(ValueError):
        calculate_vat(amount, vat_rate)

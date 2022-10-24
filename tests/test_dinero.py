import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR, GBP

unit_price = Dinero(2.32, USD)
money_received = Dinero("6.96", USD)
number_sold = 3


@pytest.mark.parametrize(
    "obj, amount, raw_type",
    [
        (Dinero(2.32, USD), 2.32, float),
        (Dinero("6.96", USD), "6.96", str),
    ],
)
def test_raw_amount(obj, amount, raw_type):
    assert obj.raw_amount == amount
    assert isinstance(obj.raw_amount, raw_type)


usd_obj = Dinero(2.32, USD)
eur_obj = Dinero(2.32, EUR)
gbp_obj = Dinero(2.32, GBP)


@pytest.mark.parametrize(
    "obj, symbol, code, exponent, precision",
    [
        (usd_obj, "$", "USD", 2, 10),
        (eur_obj, "€", "EUR", 2, 10),
        (gbp_obj, "£", "GBP", 2, 10),
    ],
)
def test_obj_properties(obj, symbol, code, exponent, precision):
    assert obj.symbol == symbol
    assert obj.code == code
    assert obj.exponent == exponent
    assert obj.precision == precision

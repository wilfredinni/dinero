from decimal import Decimal

import pytest

from dinero import Dinero
from dinero._validators import Validators
from dinero.currencies import EUR, GBP, USD
from dinero.exceptions import InvalidOperationError

unit_price = Dinero(2.32, USD)
money_received = Dinero("6.96", USD)
number_sold = 3


validate = Validators()


@pytest.mark.parametrize(
    "amount",
    [
        (Dinero(24, USD)),
        (Dinero(24.5, USD)),
        (Dinero("24.5", USD)),
    ],
)
def test_dinero_amount_validator(amount):
    assert isinstance(amount, Dinero)


@pytest.mark.parametrize(
    "amount",
    [[], (), {}, set()],
)
def test_error_dinero_amount_validator(amount):
    with pytest.raises(InvalidOperationError):
        Dinero(amount, USD)


@pytest.mark.parametrize(
    "obj, amount, raw_type",
    [
        (Dinero(2.32, USD), Decimal(2.32), Decimal),
        (Dinero("6.96", USD), Decimal(6.96), Decimal),
    ],
)
def test_raw_amount(obj, amount, raw_type):
    places = Decimal(f"1e-{USD['exponent']}")

    assert obj.raw_amount == amount.quantize(places)
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


@pytest.mark.parametrize(
    "obj, number, symbol, currency, full",
    [
        (usd_obj, "2.32", "$2.32", "2.32 USD", "$2.32 USD"),
        (eur_obj, "2.32", "€2.32", "2.32 EUR", "€2.32 EUR"),
        (gbp_obj, "2.32", "£2.32", "2.32 GBP", "£2.32 GBP"),
    ],
)
def test_obj_formatted(obj, number, symbol, currency, full):
    assert obj.format() == number
    assert obj.format(symbol=True) == symbol
    assert obj.format(currency=True) == currency
    assert obj.format(symbol=True, currency=True) == full


@pytest.mark.parametrize(
    "unit_price, units_sold, money_received",
    [
        (Dinero("2.32", USD), 3, Dinero("6.96", USD)),
        (Dinero("2.32", USD), Decimal(3), Dinero("6.96", USD)),
        (Dinero("2.32", USD), 3.0, Dinero("6.96", USD)),
        (Dinero("2.32", USD), Decimal(3.0), Dinero("6.96", USD)),
    ],
)
def test_balance_ok(unit_price, units_sold, money_received):
    assert unit_price.multiply(units_sold).eq(money_received)
    assert unit_price * units_sold == money_received


@pytest.mark.parametrize(
    "unit_price, units_sold, money_received",
    [
        (Dinero("2.38", USD), 3, Dinero("6.96", USD)),
        (Dinero("2.38", USD), Decimal(3), Dinero("6.96", USD)),
        (Dinero("2.32", USD), 2.33, Dinero("5.38", USD)),
        (Dinero("2.32", USD), Decimal(2.33), Dinero("5.38", USD)),
    ],
)
def test_balance_wrong(unit_price, units_sold, money_received):
    assert unit_price.multiply(units_sold).eq(money_received) is False
    assert unit_price * units_sold != money_received

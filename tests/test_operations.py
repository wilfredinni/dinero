import pytest

from dinero import Dinero
from dinero.currencies import USD


@pytest.mark.parametrize(
    "unit_price, units_sold, money_received",
    [
        (Dinero("2.32", USD), "3", Dinero("6.96", USD)),
        (Dinero("2.32", USD), Dinero("2.32", USD), "5.38"),
        (Dinero("2.32", USD), Dinero("2.32", USD), Dinero("5.38", USD)),
    ],
)
def test_balance_ok(unit_price, units_sold, money_received):
    assert unit_price.multiply(units_sold).equals_to(money_received)
    assert unit_price * units_sold == money_received


@pytest.mark.parametrize(
    "unit_price, units_sold, money_received",
    [
        (Dinero("2.38", USD), "3", Dinero("6.96", USD)),
        (Dinero("2.32", USD), Dinero("2.31", USD), "5.38"),
        (Dinero("2.32", USD), Dinero("2.33", USD), Dinero("5.38", USD)),
    ],
)
def test_balance_wrong(unit_price, units_sold, money_received):
    assert unit_price.multiply(units_sold).equals_to(money_received) is False
    assert unit_price * units_sold != money_received

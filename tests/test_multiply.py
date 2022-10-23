import pytest

from dinero import Dinero, DifferentCurrencyError
from dinero.currencies import USD, EUR


@pytest.mark.parametrize(
    "amount, multiplicand, total",
    [
        (Dinero("2.32", USD), "3", "6.96"),
        (Dinero("2.32", USD), Dinero("3", USD), "6.96"),
        (Dinero("2.32", USD), Dinero("3", USD), Dinero("6.96", USD)),
        (Dinero("2.32", USD), "3", Dinero("6.96", USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_multiply_amount_str(amount, multiplicand, total):
    assert amount * multiplicand == total
    assert amount.multiply(multiplicand) == total
    assert amount.multiply(multiplicand).equals_to(total)


@pytest.mark.parametrize(
    "amount, multiplicand, total",
    [
        (Dinero(2.32, USD), 3, 6.96),
        (Dinero(2.32, USD), Dinero(3, USD), 6.96),
        (Dinero(2.32, USD), Dinero(3, USD), Dinero(6.96, USD)),
        (Dinero(2.32, USD), 3, Dinero(6.96, USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_multiply_amount_number(amount, multiplicand, total):
    assert amount * multiplicand == total
    assert amount.multiply(multiplicand) == total
    assert amount.multiply(multiplicand).equals_to(total)


@pytest.mark.parametrize(
    "amount, multiplicand, total",
    [
        (Dinero(2.32, USD), Dinero("3", USD), Dinero("6.96", USD)),
        (Dinero("2.32", USD), Dinero(3, USD), Dinero("6.96", USD)),
        (Dinero("2.32", USD), Dinero("3", USD), Dinero(6.96, USD)),
        (Dinero(2.32, USD), Dinero(3, USD), Dinero("6.96", USD)),
        (Dinero("2.32", USD), Dinero(3, USD), Dinero(6.96, USD)),
        (Dinero(2.32, USD), Dinero("3", USD), Dinero(6.96, USD)),
        # ----
        (Dinero(2.32, USD), Dinero("3", USD), "6.96"),
        (Dinero("2.32", USD), Dinero(3, USD), "6.96"),
        (Dinero("2.32", USD), Dinero("3", USD), 6.96),
        (Dinero(2.32, USD), Dinero(3, USD), "6.96"),
        (Dinero("2.32", USD), Dinero(3, USD), 6.96),
        (Dinero(2.32, USD), Dinero("3", USD), 6.96),
        # ----
        (Dinero(2.32, USD), "3", Dinero("6.96", USD)),
        (Dinero("2.32", USD), 3, Dinero("6.96", USD)),
        (Dinero("2.32", USD), "3", Dinero(6.96, USD)),
        (Dinero(2.32, USD), 3, Dinero("6.96", USD)),
        (Dinero("2.32", USD), 3, Dinero(6.96, USD)),
        (Dinero(2.32, USD), "3", Dinero(6.96, USD)),
    ],
)
def test_multiply_amount_mixed(amount, multiplicand, total):
    assert amount * multiplicand == total
    assert amount.multiply(multiplicand) == total
    assert amount.multiply(multiplicand).equals_to(total)


@pytest.mark.parametrize(
    "amount, multiplicand",
    [
        (Dinero(2.32, USD), Dinero(3, EUR)),
        (Dinero(2.32, USD), Dinero("3", EUR)),
        (Dinero("2.32", USD), Dinero("3", EUR)),
        (Dinero("2.32", USD), Dinero(3, EUR)),
    ],
)
def test_different_currencies_error(amount, multiplicand):
    with pytest.raises(DifferentCurrencyError):
        amount * multiplicand

    with pytest.raises(DifferentCurrencyError):
        amount.multiply(multiplicand)

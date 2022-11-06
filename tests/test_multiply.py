import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR
from dinero.exceptions import DifferentCurrencyError, InvalidOperationError


@pytest.mark.parametrize(
    "amount, multiplicand, total",
    [
        (Dinero("2.32", USD), Dinero("3", USD), Dinero("6.96", USD)),
        (Dinero("2.32", USD), "3", Dinero("6.96", USD)),
    ],
    ids=["obj_obj_obj", "obj_str_obj"],
)
def test_multiply_amount_str(amount, multiplicand, total):
    assert amount * multiplicand == total
    assert amount.multiply(multiplicand) == total
    assert amount.multiply(multiplicand).equals_to(total)


@pytest.mark.parametrize(
    "amount, multiplicand, total",
    [
        (Dinero(2.32, USD), Dinero(3, USD), Dinero(6.96, USD)),
        (Dinero(2.32, USD), 3, Dinero(6.96, USD)),
    ],
    ids=["obj_obj_obj", "obj_str_obj"],
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


@pytest.mark.parametrize(
    "amount, addend",
    [
        (Dinero(24.5, USD), []),
        (Dinero(24.5, USD), ()),
        (Dinero("24.5", USD), {}),
    ],
)
def test_invalid_operation_error(amount, addend):
    with pytest.raises(InvalidOperationError):
        amount * addend

    with pytest.raises(InvalidOperationError):
        amount.multiply(addend)

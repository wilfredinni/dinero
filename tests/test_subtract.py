import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR
from dinero.exceptions import DifferentCurrencyError, InvalidOperationError


@pytest.mark.parametrize(
    "amount, subtrahend, total",
    [
        (Dinero("24.5", USD), "1", "23.50"),
        (Dinero("24.5", USD), Dinero("1", USD), "23.50"),
        (Dinero("24.5", USD), Dinero("1", USD), Dinero("23.50", USD)),
        (Dinero("24.5", USD), "1", Dinero("23.50", USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_subtract_amount_str(amount, subtrahend, total):
    assert amount - subtrahend == total
    assert amount.subtract(subtrahend) == total
    assert amount.subtract(subtrahend).equals_to(total)


@pytest.mark.parametrize(
    "amount, subtrahend, total",
    [
        (Dinero(24.5, USD), 1, 23.50),
        (Dinero(24.5, USD), Dinero(1, USD), 23.50),
        (Dinero(24.5, USD), Dinero(1, USD), Dinero(23.50, USD)),
        (Dinero(24.5, USD), 1, Dinero(23.50, USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_subtract_amount_number(amount, subtrahend, total):
    assert amount - subtrahend == total
    assert amount.subtract(subtrahend) == total
    assert amount.subtract(subtrahend).equals_to(total)


@pytest.mark.parametrize(
    "amount, subtrahend, total",
    [
        (Dinero(24.5, USD), Dinero("1", USD), Dinero("23.50", USD)),
        (Dinero("24.5", USD), Dinero(1, USD), Dinero("23.50", USD)),
        (Dinero("24.5", USD), Dinero("1", USD), Dinero(23.50, USD)),
        (Dinero(24.5, USD), Dinero(1, USD), Dinero("23.50", USD)),
        (Dinero("24.5", USD), Dinero(1, USD), Dinero(23.50, USD)),
        (Dinero(24.5, USD), Dinero("1", USD), Dinero(23.50, USD)),
        # ----
        (Dinero(24.5, USD), Dinero("1", USD), "23.50"),
        (Dinero("24.5", USD), Dinero(1, USD), "23.50"),
        (Dinero("24.5", USD), Dinero("1", USD), 23.50),
        (Dinero(24.5, USD), Dinero(1, USD), "23.50"),
        (Dinero("24.5", USD), Dinero(1, USD), 23.50),
        (Dinero(24.5, USD), Dinero("1", USD), 23.50),
        # ----
        (Dinero(24.5, USD), "1", Dinero("23.50", USD)),
        (Dinero("24.5", USD), 1, Dinero("23.50", USD)),
        (Dinero("24.5", USD), "1", Dinero(23.50, USD)),
        (Dinero(24.5, USD), 1, Dinero("23.50", USD)),
        (Dinero("24.5", USD), 1, Dinero(23.50, USD)),
        (Dinero(24.5, USD), "1", Dinero(23.50, USD)),
    ],
)
def test_subtract_amount_mixed(amount, subtrahend, total):
    assert amount - subtrahend == total
    assert amount.subtract(subtrahend) == total
    assert amount.subtract(subtrahend).equals_to(total)


@pytest.mark.parametrize(
    "amount, subtrahend",
    [
        (Dinero(24.5, USD), Dinero(1, EUR)),
        (Dinero(24.5, USD), Dinero("1", EUR)),
        (Dinero("24.5", USD), Dinero("1", EUR)),
        (Dinero("24.5", USD), Dinero(1, EUR)),
    ],
)
def test_different_currencies_error(amount, subtrahend):
    with pytest.raises(DifferentCurrencyError):
        amount - subtrahend

    with pytest.raises(DifferentCurrencyError):
        amount.subtract(subtrahend)


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
        amount - addend

    with pytest.raises(InvalidOperationError):
        amount.subtract(addend)

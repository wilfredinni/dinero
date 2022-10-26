import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR
from dinero.exceptions import DifferentCurrencyError, InvalidOperationError


@pytest.mark.parametrize(
    "amount, addend, total",
    [
        (Dinero("24.5", USD), "1", "25.50"),
        (Dinero("24.5", USD), Dinero("1", USD), "25.50"),
        (Dinero("24.5", USD), Dinero("1", USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), "1", Dinero("25.50", USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_add_amount_str(amount, addend, total):
    assert amount + addend == total
    assert amount.add(addend) == total
    assert amount.add(addend).equals_to(total)


@pytest.mark.parametrize(
    "amount, addend, total",
    [
        (Dinero(24.5, USD), 1, 25.50),
        (Dinero(24.5, USD), Dinero(1, USD), 25.50),
        (Dinero(24.5, USD), Dinero(1, USD), Dinero(25.50, USD)),
        (Dinero(24.5, USD), 1, Dinero(25.50, USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_add_amount_number(amount, addend, total):
    assert amount + addend == total
    assert amount.add(addend) == total
    assert amount.add(addend).equals_to(total)


@pytest.mark.parametrize(
    "amount, addend, total",
    [
        (Dinero(24.5, USD), Dinero("1", USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), Dinero(1, USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), Dinero("1", USD), Dinero(25.50, USD)),
        (Dinero(24.5, USD), Dinero(1, USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), Dinero(1, USD), Dinero(25.50, USD)),
        (Dinero(24.5, USD), Dinero("1", USD), Dinero(25.50, USD)),
        # ----
        (Dinero(24.5, USD), Dinero("1", USD), "25.50"),
        (Dinero("24.5", USD), Dinero(1, USD), "25.50"),
        (Dinero("24.5", USD), Dinero("1", USD), 25.50),
        (Dinero(24.5, USD), Dinero(1, USD), "25.50"),
        (Dinero("24.5", USD), Dinero(1, USD), 25.50),
        (Dinero(24.5, USD), Dinero("1", USD), 25.50),
        # ----
        (Dinero(24.5, USD), "1", Dinero("25.50", USD)),
        (Dinero("24.5", USD), 1, Dinero("25.50", USD)),
        (Dinero("24.5", USD), "1", Dinero(25.50, USD)),
        (Dinero(24.5, USD), 1, Dinero("25.50", USD)),
        (Dinero("24.5", USD), 1, Dinero(25.50, USD)),
        (Dinero(24.5, USD), "1", Dinero(25.50, USD)),
    ],
)
def test_add_amount_mixed(amount, addend, total):
    assert amount + addend == total
    assert amount.add(addend) == total
    assert amount.add(addend).equals_to(total)


@pytest.mark.parametrize(
    "amount, addend, total",
    [
        (Dinero(24.5, USD), Dinero("1", USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), Dinero(1, USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), Dinero("1", USD), Dinero(25.50, USD)),
        (Dinero(24.5, USD), Dinero(1, USD), Dinero("25.50", USD)),
        (Dinero("24.5", USD), Dinero(1, USD), Dinero(25.50, USD)),
        (Dinero(24.5, USD), Dinero("1", USD), Dinero(25.50, USD)),
        # ----
        (Dinero(24.5, USD), Dinero("1", USD), "25.50"),
        (Dinero("24.5", USD), Dinero(1, USD), "25.50"),
        (Dinero("24.5", USD), Dinero("1", USD), 25.50),
        (Dinero(24.5, USD), Dinero(1, USD), "25.50"),
        (Dinero("24.5", USD), Dinero(1, USD), 25.50),
        (Dinero(24.5, USD), Dinero("1", USD), 25.50),
        # ----
        (Dinero(24.5, USD), "1", Dinero("25.50", USD)),
        (Dinero("24.5", USD), 1, Dinero("25.50", USD)),
        (Dinero("24.5", USD), "1", Dinero(25.50, USD)),
        (Dinero(24.5, USD), 1, Dinero("25.50", USD)),
        (Dinero("24.5", USD), 1, Dinero(25.50, USD)),
        (Dinero(24.5, USD), "1", Dinero(25.50, USD)),
    ],
)
def test_sum_amount_mixed(amount, addend, total):
    assert sum([amount, addend, 0]) == total


@pytest.mark.parametrize(
    "amount, addend",
    [
        (Dinero(24.5, USD), Dinero(1, EUR)),
        (Dinero(24.5, USD), Dinero("1", EUR)),
        (Dinero("24.5", USD), Dinero("1", EUR)),
        (Dinero("24.5", USD), Dinero(1, EUR)),
    ],
)
def test_different_currencies_error(amount, addend):
    with pytest.raises(DifferentCurrencyError):
        amount + addend

    with pytest.raises(DifferentCurrencyError):
        amount.add(addend)


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
        amount + addend

    with pytest.raises(InvalidOperationError):
        amount.add(addend)

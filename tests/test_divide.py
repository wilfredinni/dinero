import pytest
from dinero import Dinero
from dinero.currencies import EUR, USD
from dinero.exceptions import DifferentCurrencyError, InvalidOperationError


@pytest.mark.parametrize(
    "amount, divisor, total",
    [
        (Dinero("155.5", USD), "2.5", "62.20"),
        (Dinero("155.5", USD), Dinero("2.5", USD), "62.20"),
        (Dinero("155.5", USD), Dinero("2.5", USD), Dinero("62.20", USD)),
        (Dinero("155.5", USD), "2.5", Dinero("62.20", USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_divide_amount_str(amount, divisor, total):
    assert amount / divisor == total
    assert amount.divide(divisor) == total
    assert amount.divide(divisor).equals_to(total)


@pytest.mark.parametrize(
    "amount, divisor, total",
    [
        (Dinero(155.5, USD), 2.5, 62.20),
        (Dinero(155.5, USD), Dinero(2.5, USD), 62.20),
        (Dinero(155.5, USD), Dinero(2.5, USD), Dinero(62.20, USD)),
        (Dinero(155.5, USD), 2.5, Dinero(62.20, USD)),
    ],
    ids=["obj_str_str", "obj_obj_str", "obj_obj_obj", "obj_str_obj"],
)
def test_divide_amount_number(amount, divisor, total):
    assert amount / divisor == total
    assert amount.divide(divisor) == total
    assert amount.divide(divisor).equals_to(total)


@pytest.mark.parametrize(
    "amount, divisor, total",
    [
        (Dinero(155.5, USD), Dinero("2.5", USD), Dinero("62.20", USD)),
        (Dinero("155.5", USD), Dinero(2.5, USD), Dinero("62.20", USD)),
        (Dinero("155.5", USD), Dinero("2.5", USD), Dinero(62.20, USD)),
        (Dinero(155.5, USD), Dinero(2.5, USD), Dinero("62.20", USD)),
        (Dinero("155.5", USD), Dinero(2.5, USD), Dinero(62.20, USD)),
        (Dinero(155.5, USD), Dinero("2.5", USD), Dinero(62.20, USD)),
        # ----
        (Dinero(155.5, USD), Dinero("2.5", USD), "62.20"),
        (Dinero("155.5", USD), Dinero(2.5, USD), "62.20"),
        (Dinero("155.5", USD), Dinero("2.5", USD), 62.20),
        (Dinero(155.5, USD), Dinero(2.5, USD), "62.20"),
        (Dinero("155.5", USD), Dinero(2.5, USD), 62.20),
        (Dinero(155.5, USD), Dinero("2.5", USD), 62.20),
        # ----
        (Dinero(155.5, USD), "2.5", Dinero("62.20", USD)),
        (Dinero("155.5", USD), 2.5, Dinero("62.20", USD)),
        (Dinero("155.5", USD), "2.5", Dinero(62.20, USD)),
        (Dinero(155.5, USD), 2.5, Dinero("62.20", USD)),
        (Dinero("155.5", USD), 2.5, Dinero(62.20, USD)),
        (Dinero(155.5, USD), "2.5", Dinero(62.20, USD)),
    ],
)
def test_divide_amount_mixed(amount, divisor, total):
    assert amount / divisor == total
    assert amount.divide(divisor) == total
    assert amount.divide(divisor).equals_to(total)


@pytest.mark.parametrize(
    "amount, divisor",
    [
        (Dinero(155.5, USD), Dinero(2.5, EUR)),
        (Dinero(155.5, USD), Dinero("2.5", EUR)),
        (Dinero("155.5", USD), Dinero("2.5", EUR)),
        (Dinero("155.5", USD), Dinero(2.5, EUR)),
    ],
)
def test_different_currencies_error(amount, divisor):
    with pytest.raises(DifferentCurrencyError):
        amount / divisor

    with pytest.raises(DifferentCurrencyError):
        amount.divide(divisor)


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
        amount / addend

    with pytest.raises(InvalidOperationError):
        amount.divide(addend)

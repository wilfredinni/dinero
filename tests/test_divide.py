from decimal import Decimal

import pytest

from dinero import Dinero
from dinero.currencies import USD
from dinero.exceptions import InvalidOperationError


@pytest.mark.parametrize(
    "amount, divisor, total",
    [
        (Dinero("155.5", USD), 2.5, Dinero("62.20", USD)),
        (Dinero("155.5", USD), Decimal(2.5), Dinero("62.20", USD)),
        (Dinero("200", USD), 2, Dinero(100, USD)),
        (Dinero("200", USD), Decimal(2), Dinero(100, USD)),
    ],
)
def test_divide_amount(amount, divisor, total):
    assert amount / divisor == total
    assert amount.divide(divisor) == total
    assert amount.divide(divisor).equals_to(total)


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
        amount / addend  # type: ignore

    with pytest.raises(InvalidOperationError):
        amount.divide(addend)

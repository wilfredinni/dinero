import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR
from dinero.exceptions import InvalidOperationError


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24.5, USD), Dinero(24.5, USD)),
        (Dinero(22.9934534, USD), Dinero(22.9934534, USD)),
    ],
)
def test_equal(obj_1, obj_2):
    assert obj_1 == obj_2
    assert obj_1.equals_to(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24.5, USD), Dinero(24, USD)),
        (Dinero(24.5, USD), Dinero(24.5, EUR)),
        (Dinero(22.9934534, USD), Dinero(22.9234539, USD)),
    ],
)
def test_not_equal(obj_1, obj_2):
    assert obj_1 != obj_2
    assert obj_1.equals_to(obj_2) is False


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24, USD), Dinero(25, USD)),
        (Dinero(24.5, USD), Dinero(24.6, USD)),
    ],
)
def test_less_than(obj_1, obj_2):
    assert obj_1 < obj_2
    assert obj_1.less_than(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24, USD), Dinero(25, USD)),
        (Dinero(24.5, USD), Dinero(24.6, USD)),
        (Dinero(24.5, USD), Dinero(24.5, USD)),
    ],
)
def test_less_than_or_equal(obj_1, obj_2):
    assert obj_1 <= obj_2
    assert obj_1.less_than_or_equal(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(25, USD), Dinero(24, USD)),
        (Dinero(24.6, USD), Dinero(24.5, USD)),
    ],
)
def test_greater_than(obj_1, obj_2):
    assert obj_1 > obj_2
    assert obj_1.greater_than(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(25, USD), Dinero(24, USD)),
        (Dinero(24.6, USD), Dinero(24.5, USD)),
        (Dinero(24.5, USD), Dinero(24.5, USD)),
    ],
)
def test_greater_than_or_equal(obj_1, obj_2):
    assert obj_1 >= obj_2
    assert obj_1.greater_than_or_equal(obj_2)


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
        amount == addend

    with pytest.raises(InvalidOperationError):
        amount.equals_to(addend)

    with pytest.raises(InvalidOperationError):
        amount < addend

    with pytest.raises(InvalidOperationError):
        amount.less_than(addend)

    with pytest.raises(InvalidOperationError):
        amount >= addend

    with pytest.raises(InvalidOperationError):
        amount.less_than_or_equal(addend)

    with pytest.raises(InvalidOperationError):
        amount > addend

    with pytest.raises(InvalidOperationError):
        amount.greater_than(addend)

    with pytest.raises(InvalidOperationError):
        amount >= addend

    with pytest.raises(InvalidOperationError):
        amount.greater_than_or_equal(addend)

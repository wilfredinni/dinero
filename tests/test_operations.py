import pytest

from dinero import Dinero
from dinero.currencies import USD
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
    assert obj_1.eq(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24.5, USD), Dinero(24, USD)),
        (Dinero(22.9934534, USD), Dinero(22.9234539, USD)),
    ],
)
def test_not_equal(obj_1, obj_2):
    assert obj_1 != obj_2
    assert obj_1.eq(obj_2) is False


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24, USD), Dinero(25, USD)),
        (Dinero(24.5, USD), Dinero(24.6, USD)),
    ],
)
def test_lt(obj_1, obj_2):
    assert obj_1 < obj_2
    assert obj_1.lt(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24, USD), Dinero(25, USD)),
        (Dinero(24.5, USD), Dinero(24.6, USD)),
        (Dinero(24.5, USD), Dinero(24.5, USD)),
    ],
)
def test_lte(obj_1, obj_2):
    assert obj_1 <= obj_2
    assert obj_1.lte(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(25, USD), Dinero(24, USD)),
        (Dinero(24.6, USD), Dinero(24.5, USD)),
    ],
)
def test_gt(obj_1, obj_2):
    assert obj_1 > obj_2
    assert obj_1.gt(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(25, USD), Dinero(24, USD)),
        (Dinero(24.6, USD), Dinero(24.5, USD)),
        (Dinero(24.5, USD), Dinero(24.5, USD)),
    ],
)
def test_gte(obj_1, obj_2):
    assert obj_1 >= obj_2
    assert obj_1.gte(obj_2)


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
        amount == addend  # type: ignore

    with pytest.raises(InvalidOperationError):
        amount.eq(addend)

    with pytest.raises(InvalidOperationError):
        amount < addend  # type: ignore

    with pytest.raises(InvalidOperationError):
        amount.lt(addend)

    with pytest.raises(InvalidOperationError):
        amount >= addend  # type: ignore

    with pytest.raises(InvalidOperationError):
        amount.lte(addend)

    with pytest.raises(InvalidOperationError):
        amount > addend  # type: ignore

    with pytest.raises(InvalidOperationError):
        amount.gt(addend)

    with pytest.raises(InvalidOperationError):
        amount >= addend  # type: ignore

    with pytest.raises(InvalidOperationError):
        amount.gte(addend)

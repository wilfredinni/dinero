import pytest

from dinero import Dinero
from dinero.currencies import USD, EUR


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24.5, USD), Dinero(24.5, USD)),
        (Dinero(24.5, USD), 24.5),
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
        (Dinero(24.5, USD), 24.4),
    ],
)
def test_not_equal(obj_1, obj_2):
    assert obj_1 != obj_2
    assert obj_1.equals_to(obj_2) is False


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24, USD), Dinero(25, USD)),
        (Dinero(24.5, USD), 24.6),
    ],
)
def test_less_than(obj_1, obj_2):
    assert obj_1 < obj_2
    assert obj_1.less_than(obj_2)


@pytest.mark.parametrize(
    "obj_1, obj_2",
    [
        (Dinero(24, USD), Dinero(25, USD)),
        (Dinero(24.5, USD), 24.6),
        (Dinero(24.5, USD), 24.5),
    ],
)
def test_less_than_or_equal(obj_1, obj_2):
    assert obj_1 <= obj_2
    assert obj_1.less_than_or_equal(obj_2)

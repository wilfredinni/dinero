import pytest

from dinero import Dinero
from dinero.currencies import USD


@pytest.mark.parametrize(
    "amount",
    [
        (Dinero("3333.259", USD)),
        (Dinero(3333.259, USD)),
    ],
    ids=["obj_str", "obj_int"],
)
def test_unformatted_dict(amount):
    expected_unformatted_result = {
        "amount": "3333.26",
        "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"},
    }
    assert amount.to_dict() == expected_unformatted_result


@pytest.mark.parametrize(
    "amount",
    [
        (Dinero("3333.259", USD)),
        (Dinero(3333.259, USD)),
    ],
    ids=["obj_str", "obj_int"],
)
def test_formatted_dict(amount):
    expected_result = {
        "amount": "3,333.26",
        "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"},
    }
    assert amount.to_dict(amount_with_format=True) == expected_result


@pytest.mark.parametrize(
    "amount",
    [
        (Dinero("3333.2", USD)),
        (Dinero(3333.2, USD)),
    ],
    ids=["obj_str", "obj_str"],
)
def test_unformatted_json(amount):
    expected_result = '{"amount": "3333.20", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'  # noqa: E501
    assert amount.to_json() == expected_result


@pytest.mark.parametrize(
    "amount",
    [
        (Dinero("3333.2", USD)),
        (Dinero(3333.2, USD)),
    ],
    ids=["obj_str", "obj_str"],
)
def test_formatted_json(amount):
    expected_result = '{"amount": "3,333.20", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'  # noqa: E501
    assert amount.to_json(amount_with_format=True) == expected_result

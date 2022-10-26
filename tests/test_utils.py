import json

import pytest
from dinero import Dinero
from dinero._utils import DecimalEncoder
from dinero.currencies import EUR, USD


def test_decimal_encoder():
    encoder = DecimalEncoder()
    assert encoder.default(Dinero("12.3", USD)._normalize(quantize=True)) == "12.30"
    assert encoder.default(Dinero(12.3, USD)._normalize(quantize=True)) == "12.30"
    assert encoder.default(Dinero("12.3", USD)._normalize()) == "12.3"
    assert encoder.default(Dinero(12.3, USD)._normalize()) == "12.3"

    to_json = {
        "amount": Dinero("12.3", EUR)._normalize(quantize=True),
        "currency": "EUR",
        "symbol": "$",
    }

    expected_result = '{"amount": "12.30", "currency": "EUR", "symbol": "$"}'
    assert json.dumps(to_json, cls=DecimalEncoder) == expected_result

    to_json = {
        "amount": Dinero("12.3", EUR)._normalize(),
        "currency": "EUR",
        "symbol": "$",
    }

    expected_result = '{"amount": "12.3", "currency": "EUR", "symbol": "$"}'
    assert json.dumps(to_json, cls=DecimalEncoder) == expected_result


@pytest.mark.parametrize(
    "amount, formatted_amount",
    [
        (Dinero("2444.5", USD), "2,444.50"),
        (Dinero("2444.56", USD), "2,444.56"),
        (Dinero("2444.566", USD), "2,444.57"),
    ],
)
def test_amount_formatter(amount, formatted_amount):
    assert amount._formatted_amount == formatted_amount

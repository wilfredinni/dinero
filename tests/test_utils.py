import json
from decimal import Decimal

import pytest
from dinero import Dinero
from dinero._utils import DecimalEncoder, amount_formatter
from dinero.currencies import EUR, USD


def test_decimal_encoder():
    encoder = DecimalEncoder()
    assert encoder.default(Dinero("12.3", USD).normalized_amount) == "12.30"
    assert encoder.default(Dinero(12.3, USD).normalized_amount) == "12.30"

    to_json = {
        "amount": Dinero("12.3", EUR).normalized_amount,
        "currency": "EUR",
        "symbol": "$",
    }

    expected_result = '{"amount": "12.30", "currency": "EUR", "symbol": "$"}'
    assert json.dumps(to_json, cls=DecimalEncoder) == expected_result


@pytest.mark.parametrize(
    "amount, exponent, formatted_amount",
    [
        (Dinero("2444.5", USD).normalized_amount, USD["exponent"], "2,444.50"),
        (Decimal("2444.5"), USD["exponent"], "2,444.50"),
    ],
)
def test_amount_formatter(amount, exponent, formatted_amount):
    assert amount_formatter(amount, exponent) == formatted_amount

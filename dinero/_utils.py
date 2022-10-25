import json

from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # if passed in object is instance of Decimal
        # convert it to a string, otherwise use the,
        # default behavior
        return (
            str(obj)
            if isinstance(obj, Decimal)
            else json.JSONEncoder.default(self, obj)
        )


def amount_formatter(amount: Decimal, exponent: int) -> str:
    currency_format = f",.{exponent}f"
    return f"{amount:{currency_format}}"

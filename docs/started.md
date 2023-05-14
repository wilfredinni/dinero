# Getting Started

## Install

```bash
pip install dinero
```

## Initialization

To create a `Dinero` object, you need an `amount` that can be an `int`, `float`, `str` or `Decimal`, and a `currency`:

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero(100.4, USD)
```

## Properties

Every `Dinero` object has the following properties:

```python
>>> amount.raw_amount
Decimal('100.40')
```

```python
>>> amount.symbol
'$'
```

```python
>>> amount.code
'USD'
```

```python
>>> amount.exponent
2
```

```python
>>> amount.precision
10
```

## Formatting

### String

You can return a formatted string representation of `Dinero` with the `format` method:

```python
>>> Dinero(2.32, EUR).format()
'2.32'
```

```python
>>> Dinero(2.32, EUR).format(symbol=True)
'€2.32'
```

```python
>>> Dinero(2.32, EUR).format(currency=True)
'2.32 EUR'
```

```python
>>> Dinero(2.32, EUR).format(symbol=True, currency=True)
'€2.32 EUR'
```

### Dictionary

Return a `Dinero` instance as a Python Dictionary:

```python title="amount_with_format=False"
>>> Dinero("3333.259", USD).to_dict()
{
    'amount': '3333.26',
    'currency':
        {
            'code': 'USD',
            'base': 10,
            'exponent': 2,
            'symbol': '$'
        }
}
```

```python title="amount_with_format=True"
>>> Dinero('3333.26', USD).to_dict(amount_with_format=True)
{
    'amount': '3,333.26',
    'currency':
        {
            'code': 'USD',
            'base': 10,
            'exponent': 2,
            'symbol': '$'
        }
}
```

### Json

Return a `Dinero` instance as a `JSON` string:

```python title="amount_with_format=False"
>>> Dinero('2,00', USD).to_json()
'{"amount": "3333.20", "currency": {"code": "USD", "base": 10...'
```

```python title="amount_with_format=True"
>>> Dinero('2,00', USD).to_json(amount_with_format=True)
'{"amount": "3,333.26", "currency": {"code": "USD", "base": 10...'
```

## Operations

If the addend or subtrahend is an `str`, `int`, `float` or `Decimal`, it will be transformed, under the hood, to a Dinero instance using the same currency:

```python title='Addition'
# those operations
Dinero(1000, USD).add(Dinero(1000, USD))
Dinero(1000, USD) + Dinero(1000, USD)

# are equivalent to
Dinero(1000, USD).add(1000)
Dinero(1000, USD) + 1000
```

```python title='Subtraction'
# those operations
Dinero(1000, USD).subtract(Dinero(100, USD))
Dinero(1000, USD) - Dinero(100, USD)

# are equivalent to
Dinero(1000, USD).subtract(1000)
Dinero(1000, USD) - 100
```

Additions and subtractions must be between instances with the same `currency`:

```python title='DifferentCurrencyError'
>>> total = Dinero(100, USD) + Dinero(100, EUR)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/.../dinero/_dinero.py", line 120, in __add__
    addend_obj = self._get_instance(addend)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/.../dinero/_dinero.py", line 74, in _get_instance
    raise DifferentCurrencyError("Currencies can not be different")
dinero.exceptions.DifferentCurrencyError: Currencies can not be different
```

The multiplicand and divisor can be `int`, `float` or of `Decimal` type:

```python title='Multiplication'
Dinero(1000, USD).multiply(2)
Dinero(1000, USD) * 2
```

```python title='Division'
Dinero(1000, USD).divide(2)
Dinero(1000, USD) / 2
```

## Comparisons

```python title='Equals to'
Dinero(1000, USD).equals_to(Dinero(1000, USD))
Dinero(1000, USD) == Dinero(1000, USD)
```

```python title='Less than'
Dinero(1000, USD).less_than(Dinero(1000, USD))
Dinero(1000, USD) < Dinero(1000, USD)
```

```python title='Less than or equal'
Dinero(1000, USD).less_than_or_equal(Dinero(1000, USD))
Dinero(1000, USD) <= Dinero(1000, USD)
```

```python title='Greater than'
Dinero(1000, USD).greater_than(Dinero(1000, USD))
Dinero(1000, USD) > Dinero(1000, USD)
```

```python title='Greater than or equal'
Dinero(1000, USD).greater_than_or_equal(Dinero(1000, USD))
Dinero(1000, USD) >= Dinero(1000, USD)
```

You can only compare to other `Dinero` objects:

```python title='InvalidOperationError'
>>> Dinero(100, USD) == 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/.../dinero/_dinero.py", line 146, in __eq__
    self._comparison_amount(amount)
  File "/home/.../dinero/_dinero.py", line 103, in _comparison_amount
    raise InvalidOperationError(InvalidOperationError.comparison_msg)
dinero.exceptions.InvalidOperationError: You can only compare against other Dinero instances.
```

## Tools

Dinero give you access to some useful tools that allow you to perform common monetary calculations, like calculating percentages, VAT, simple and compound interests, etc.

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_compound_interest

principal = Dinero("2000", USD)
total_interest = calculate_compound_interest(
    principal=principal,
    interest_rate=5, # 5% interest rate
    duration=10, # 10 year loan duration
    compound_frequency=12, # interest compounded monthly
)
total_interest.format(symbol=True, currency=True)
'$1,294.02 USD'
```

See al the available tools in the [tools](/dinero/tools/) section.

## Currencies

The currency is one of the two pieces necessary to create a Dinero object.

A Dinero currency is composed of:

- A unique code.
- A base, or radix.
- An exponent.
- A symbol (optional)

```python
EUR: Currency = {
    "code": "EUR",
    "base": 10,
    "exponent": 2,
    "symbol": "€",
}
```

More about [currencies](/dinero/currencies).

### Custom Currencies

You can easily create custom currencies:

```python
from dinero import Dinero

BTC = {
    "code": "BTC",
    "base": 10,
    "exponent": 2,
    "symbol": "₿",
}

Dinero(1000.5, BTC)
```

More about [custom currencies](/dinero/currencies/#custom-currencies).

### Type hints

If you are using `type hints` in your project you would want to import `dinero.types.Currency` to prevent warnings:

```python title='dinero.types.Currency'
class Currency(TypedDict):
    code: str
    base: int
    exponent: int
    symbol: NotRequired[str]
```

```python
from dinero.types import Currency

BTC: Currency = {
    "code": "BTC",
    "base": 10,
    "exponent": 2,
    "symbol": "₿",
}

Dinero(1000.5, BTC)
```

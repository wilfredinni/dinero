# Getting Started

## Install

Dinero is a dependency free project.

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

```python title='Addition'
Dinero(1000, USD).add(Dinero(1000, USD))
Dinero(1000, USD) + Dinero(1000, USD)
```

```python title='Subtraction'
Dinero(1000, USD).subtract(Dinero(100, USD))
Dinero(1000, USD) - Dinero(100, USD)
```

```python title='Multiplication'
Dinero(1000, USD).multiply(2)
Dinero(1000, USD) * 2
```

```python title='Division'
Dinero(1000, USD).divide(2)
Dinero(1000, USD) / 2
```

If a `Dinero` object is operated against an `int`, `float`, `str` or `Decimal`, that value will be transformed to a `Dinero` instance using the same currency:

```python title='Addition'
Dinero(1000, USD).add(1000)
Dinero(1000, USD) + 1000
```

```python title='Subtraction'
Dinero(1000, USD).subtract(100)
Dinero(1000, USD) - 100
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

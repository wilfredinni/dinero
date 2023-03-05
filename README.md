<h1 align="center"> Dinero: Make exact monetary calculations</h1>

<p align="center">
<a href="https://pypi.org/project/dinero/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/dinero">
</a>
<a href="https://pypi.org/project/dinero/">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/dinero">
</a>
<a href="https://github.com/wilfredinni/dinero/actions">
  <img alt="Build status" src="https://github.com/wilfredinni/dinero/actions/workflows/test.yml/badge.svg" data-canonical-src="https://img.shields.io/github/workflow/status/Delgan/loguru/Tests/master" style="max-width: 100%;">
</a>
<a href="https://codecov.io/github/wilfredinni/dinero" >
 <img alt="Codecov" src="https://img.shields.io/codecov/c/github/wilfredinni/dinero">
</a>
<a href="https://www.codacy.com/gh/wilfredinni/dinero/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wilfredinni/dinero&amp;utm_campaign=Badge_Grade">
 <img alt="Codacy grade" src="https://img.shields.io/codacy/grade/d6b13235aec14905968fb4b0e9a5e8fd">
</a>
<a href="https://github.com/wilfredinni/dinero/blob/master/LICENSE">
  <img alt="PyPI - License" src="https://img.shields.io/pypi/l/dinero">
</a>
</p>

<p align="center">
  <img width="300" height="200" src="https://media.tenor.com/EWRvErYGzPUAAAAC/bugs-bunny-looney-tunes.gif">
</p>

This project is inspired by the excellent [dinero.js](https://github.com/dinerojs/dinero.js) library.

Python Decimal instances are enough for basic monetary calculations, but when you face more complex use-cases they often show limitations and are not so intuitive to work with. Dinero provides a cleaner and easier to use API while still relying on the standard library. So it's still Decimal, but easier.

[Read the Documentation](https://wilfredinni.github.io/dinero/)

## The problem

> Using floats to do exact calculations in Python can be dangerous. When you try to find out how much 2.32 x 3 is, Python tells you it's 6.959999999999999. For some calculations, that’s fine. But if you are calculating a transaction involving money, that’s not what you want to see. Sure, you could round it off, but that's a little hacky.

```python
>>> 2.32 * 3 == 6.96
False
>>> 2.32 * 3
6.959999999999999
```

You can read [How to Count Money Exactly in Python](https://learnpython.com/blog/count-money-python/) to get a better idea.

## Why Dinero?

A `Dinero` object is an immutable data structure representing a specific monetary value. It comes with methods for creating, parsing, manipulating, testing and formatting.

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

```python
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

```python
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

```python
>>> Dinero('2,00', USD).to_json()
'{"amount": "3333.20", "currency": {"code": "USD", "base": 10...'
```

```python
>>> Dinero('2,00', USD).to_json(amount_with_format=True)
'{"amount": "3,333.26", "currency": {"code": "USD", "base": 10...'
```

## Operations

If the addend or subtrahend is an `str`, `int`, `float` or `Decimal`, it will be transformed, under the hood, to a Dinero instance using the same currency:

```python
# those operations
Dinero(1000, USD).add(Dinero(1000, USD))
Dinero(1000, USD) + Dinero(1000, USD)

# are equivalent to
Dinero(1000, USD).add(1000)
Dinero(1000, USD) + 1000
```

```python
# those operations
Dinero(1000, USD).subtract(Dinero(100, USD))
Dinero(1000, USD) - Dinero(100, USD)

# are equivalent to
Dinero(1000, USD).subtract(1000)
Dinero(1000, USD) - 100
```

Additions and subtractions must be between instances with the same `currency`:

```python
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

```python
Dinero(1000, USD).multiply(2)
Dinero(1000, USD) * 2
```

```python
Dinero(1000, USD).divide(2)
Dinero(1000, USD) / 2
```

## Comparisons

```python
Dinero(1000, USD).equals_to(Dinero(1000, USD))
Dinero(1000, USD) == Dinero(1000, USD)
```

```python
Dinero(1000, USD).less_than(Dinero(1000, USD))
Dinero(1000, USD) < Dinero(1000, USD)
```

```python
Dinero(1000, USD).less_than_or_equal(Dinero(1000, USD))
Dinero(1000, USD) <= Dinero(1000, USD)
```

```python
Dinero(1000, USD).greater_than(Dinero(1000, USD))
Dinero(1000, USD) > Dinero(1000, USD)
```

```python
Dinero(1000, USD).greater_than_or_equal(Dinero(1000, USD))
Dinero(1000, USD) >= Dinero(1000, USD)
```

You can only compare to other `Dinero` objects:

```python
>>> Dinero(100, USD) == 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/.../dinero/_dinero.py", line 146, in __eq__
    self._comparison_amount(amount)
  File "/home/.../dinero/_dinero.py", line 103, in _comparison_amount
    raise InvalidOperationError(InvalidOperationError.comparison_msg)
dinero.exceptions.InvalidOperationError: You can only compare against other Dinero instances.
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

```python
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

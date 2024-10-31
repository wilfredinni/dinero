<div align="center">

# Dinero
### Make exact monetary calculations.

[![PyPI][pypi-badge]][pypi-url]
[![Build Status][build-badge]][build-url]
[![CodeQL Status](https://github.com/wilfredinni/dinero/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/wilfredinni/dinero/actions/workflows/github-code-scanning/codeql)
[![Codecov][codecov-badge]][codecov-url]
[![License][license-badge]][license-url]

<!-- Badge URLs -->
[pypi-badge]: https://img.shields.io/pypi/v/dinero
[build-badge]: https://github.com/wilfredinni/dinero/actions/workflows/test.yml/badge.svg
[codecov-badge]: https://img.shields.io/codecov/c/github/wilfredinni/dinero
[license-badge]: https://img.shields.io/pypi/l/dinero

<!-- Links -->
[pypi-url]: https://pypi.org/project/dinero/
[build-url]: https://github.com/wilfredinni/dinero/actions
[codecov-url]: https://codecov.io/github/wilfredinni/dinero
[license-url]: https://github.com/wilfredinni/dinero/blob/master/LICENSE
</div>

This project is inspired by the excellent [dinero.js](https://github.com/dinerojs/dinero.js) library.

Python Decimal instances are enough for basic monetary calculations, but when you face more complex use-cases they often show limitations and are not so intuitive to work with. Dinero provides a cleaner and easier to use API while still relying on the standard library. So it's still Decimal, but easier.

[Read the Documentation](https://wilfredinni.github.io/dinero/)

## Install

```bash
pip install dinero
```

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

A `Dinero` object represent a specific monetary value. It comes with methods for creating, parsing, manipulating, testing and formatting.

```python
>>> from dinero import Dinero
>>> from dinero.currencies import USD
>>>
>>> Dinero(2.32, USD) * 3 == Dinero(6.96. USD)
True
```

### Currencies

Dinero give you access to more than 100 different currencies:

```python
>>> from dinero.currencies import USD, EUR, GBP, INR, CLP
```

```python
>>> amount = Dinero(2.32, EUR)
>>> amount.format(symbol=True, currency=True)
'€2.32 EUR'
>>>
>>> amount.raw_amount
Decimal('2.32')
```

More about [currencies](https://wilfredinni.github.io/dinero/currencies/).

### Operations

Operations can be performed between Dinero objects or between Dinero objects and numbers:


```python
>>> total = Dinero(456.343567, USD) + 345.32 *  3
>>> print(total)
# 1,492.30
```

```python
>>> total = (Dinero(345.32, USD).multiply(3)).add(456.343567)
>>> print(total)
# 1,492.30
```

More about [operations](https://wilfredinni.github.io/dinero/started/#operations).

### Comparisons

Dinero objects can be compared to each other by using Python comparison operators:

```python
>>> Dinero(100, EUR) == Dinero(100, EUR)
True
```

```python
>>> Dinero(100, EUR).equals_to(Dinero(100, EUR))
True
```

More about [comparisons](https://wilfredinni.github.io/dinero/started/#comparisons).

### Tools

Dinero give you access to some useful tools that allow you to perform common monetary calculations, like percentages, VAT, simple and compound interests, etc.

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_compound_interest

principal = Dinero("2000", USD)
total_interest = calculate_compound_interest(
    principal=principal,
    interest_rate=5,
    duration=10,
    compound_frequency=12,
)
total_interest.format(symbol=True, currency=True)
'$1,294.02 USD'
```

See all the available tools in the [tools](https://wilfredinni.github.io/dinero/tools/) section.

### Custom currencies

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

```python
Dinero(amount=1000.5, currency={'code': 'BTC', 'base': 10, 'exponent': 2, 'symbol': '₿'})
```

More about [custom currencies](https://wilfredinni.github.io/dinero/currencies/#custom-currencies).
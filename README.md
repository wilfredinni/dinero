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

Operations can be performed between Dinero objects or between Dinero objects and numbers by using Python operators or its own methods:


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

Dinero objects can be compared to each other by using Python comparison operators or by using its own methods:

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
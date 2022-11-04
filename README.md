<h1 align="center"> Dinero: Make exact monetary calculations</h1>

<p align="center">
<a href="https://codecov.io/github/wilfredinni/dinero" > 
 <img src="https://codecov.io/github/wilfredinni/dinero/branch/master/graph/badge.svg?token=XQA8OA1Z9W"/> 
 </a>
<img alt="test" src="https://github.com/wilfredinni/dinero/actions/workflows/test.yml/badge.svg" />
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/dinero">
<img alt="PyPI" src="https://img.shields.io/pypi/v/dinero">
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/dinero">
</p>

<p align="center">
  <img width="300" height="200" src="https://media.tenor.com/EWRvErYGzPUAAAAC/bugs-bunny-looney-tunes.gif">
</p>


This project is inspired by the excellent [dinero.js](https://github.com/dinerojs/dinero.js) library.

A `Dinero` object is an immutable data structure representing a specific monetary value. It comes with methods for creating, parsing, manipulating, testing and formatting them.

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

Python `Decimal` instances are enough for basic cases but when you face more complex use-cases they often show limitations and are not so intuitive to work with. Dinero provides a cleaner and more easy to use API while still relying on the standard library. So it's still `Decimal` but easier.

```python
>>> from dinero import Dinero
>>> from dinero.currencies import USD
>>>
>>> Dinero(2.32, USD) * 3 == 6.96
True
```

### Currencies

Dinero give you access to more than 100 different currencies:

```python
>>> from dinero.currencies import USD, EUR, GBP, INR, CLP
```

```python
>>> Dinero(2.32, EUR)
Dinero(amount=2.32, currency={'code': 'EUR', 'base': 10, 'exponent': 2, 'symbol': '€'})
```

```python
>>> Dinero(2.32, EUR).format(symbol=True, currency=True)
'€2.32 EUR'
```

```python
>>> Dinero(2.32, EUR).raw_amount
Decimal('2.32')
```

### Operations

```python
>>> total = Dinero(456.343567, USD) + 345.32 *  3
>>> print(total)
# 1,492.30
```

```python
>>> product = Dinero(345.32, USD).multiply(3)
>>> total = product.add(456.343567)
>>> print(total)
# 1,492.30
```

### Comparisons

```python
>>> Dinero(100, EUR) == Dinero(100, EUR)
True
```

```python
>>> Dinero(100, EUR).equals_to(Dinero(100, EUR))
True
```

```python
>>> Dinero(100, EUR) == 100
True
```

```python
>>> Dinero(100, EUR).equals_to(100)
True
```

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

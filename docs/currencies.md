# Currencies

The currency is one of the two pieces of domain data necessary to create a Dinero object.

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

## Currency elements

### Code

The currency code is a unique identifier for the currency. By convention, they're usually a three-letter or number. For example, in the case of national [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currencies, the first two letters of the code are the two letters of the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, and the third is usually the initial of the currency itself.

```python
USD: Currency = {
    "code": "USD",
    # ...
}
```

### Base

The currency base (or radix) is the number of unique digits used to represent a currency's minor unit. Most currencies in circulation are decimal, meaning their base is 10.

```python
USD: Currency = {
    "code": "USD",
    "base": 10,
    # ...
}
```

There are still non-decimal currencies in circulation, such as the Mauritanian ouguiya and the Malagasy ariary.

```python
MRU: Currency = {
    "code": "MRU",
    "base": 5,
    # ...
}
```

Some currencies have multiple subdivisions. For example, before decimalization, the British pound sterling was divided into 20 shillings, and each shilling into 12 pence. You also have examples in fiction, like Harry Potter, where one Galleon is divided into 17 Sickles, and each Sickle into 29 Knuts.

To represent these currencies, you can take how many of the smallest subdivision there are in the major one. There are 240 pence in a pound sterling, and in Harry Potter, 493 Knuts in a Galleon.

```python
GBW = {
    "code": "GBW",
    "base": 493,
    "exponent": 1,
}
```

### Exponent

The currency exponent expresses the decimal relationship between the currency and its minor unit. For example, there are 100 cents in a US dollar, being 10 to the power of 2, so the exponent for the US dollar is 2.

```python
USD: Currency = {
    "code": "USD",
    "base": 10,
    "exponent": 2,
}
```

An easier way to think about it is as the number of digits after the decimal separator.

When a currency doesn't have minor currency units (e.g., the Japanese yen), the exponent should be 0. In this case, you can express the amount in major currency units.

```python
JPY: Currency = {
    "code": "JPY",
    "base": 10,
    "exponent": 0,
    "symbol": "¥",
}
```

### Symbol

The symbol that represents the currency. If not specified, it will default to `$`.

```python
JPY: Currency = {
    "code": "JPY",
    "base": 10,
    "exponent": 0,
    "symbol": "¥",
}
```

## Custom Currencies

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
from dinero.types import Currency

BTC: Currency = {
    "code": "BTC",
    "base": 10,
    "exponent": 2,
    "symbol": "₿",
}

Dinero(1000.5, BTC)
```


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

There are still non-decimal currencies in circulation, such as the Mauritanian ouguiya and the Malagasy ariary, which have a base of 5.

```python
MRU: Currency = {
    "code": "MRU",
    "base": 5,
    "exponent": 1, # 1 Ouguiya = 5 Khoums
    # ...
}
```
For currencies with complex subdivisions not fitting a simple base/exponent model (e.g., historical currencies or fictional ones with multiple tiers like Galleons, Sickles, Knuts), it's best to choose the smallest unit of the currency (e.g., Knuts) as the fundamental unit for calculations. The `amount` in Dinero objects would then represent quantities of this smallest unit. Conversions to larger units (Galleons, Sickles) would be handled at the application level.

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
from dinero.types import Currency # Recommended for type hinting

BTC: Currency = {
    "code": "BTC",
    "base": 10,      # Standard for decimal-based representation
    "exponent": 8,   # Bitcoin is typically represented with 8 decimal places (Satoshis)
    "symbol": "₿",
}

# Initialize with a string for precision, representing 1000.50 BTC
btc_amount = Dinero("1000.50000000", BTC)
print(btc_amount.format(symbol=True)) # Outputs: ₿1,000.50000000

# Example representing 1 Satoshi (0.00000001 BTC)
one_satoshi = Dinero("0.00000001", BTC)
print(one_satoshi.format(currency=True)) # Outputs: 0.00000001 BTC
```

When defining custom currencies, especially for cryptocurrencies or other systems with many decimal places, ensure the `exponent` correctly reflects the number of subunits you intend to work with. The `base` is typically 10 for these.

### Type hints

If you are using `type hints` in your project you would want to import `dinero.types.Currency` to prevent warnings:

```python
from dinero import Dinero # Ensure Dinero is imported for the example
from dinero.types import Currency

BTC_definition: Currency = { # Renamed to avoid conflict with BTC above if in same scope
    "code": "BTC",
    "base": 10,
    "exponent": 8, # Consistent with the example above (8 decimal places for Bitcoin)
    "symbol": "₿",
}

# Example of creating a Dinero object with the typed currency definition
my_btc_balance = Dinero("0.12345678", BTC_definition)
print(my_btc_balance.format(symbol=True, currency=True)) # Outputs: ₿0.12345678 BTC
```


<div align="center">

# Dinero
### Precise, Type-Safe Monetary Calculations in Python

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

Dinero is a modern Python library that brings precision and type safety to monetary calculations. Built on Python's `Decimal` type, it provides an intuitive API for financial operations while ensuring accuracy and maintainability.

[📚 Read the Full Documentation](https://wilfredinni.github.io/dinero/)

## Key Features

- 🎯 **Precise Calculations**: Built on Python's `Decimal` type for exact monetary computations
- 🔒 **Type Safety**: Full type hint support and runtime validation
- 🌍 **Currency Support**: Over 100 currencies following ISO 4217 standards
- 🧮 **Financial Tools**: Built-in support for VAT, interest calculations, markup, and more
- 🔄 **Immutable Objects**: Thread-safe with predictable behavior
- 💪 **Modern Python**: Type hints, clean API, and comprehensive test coverage

## Why Dinero?

Working with money in Python can be tricky due to floating-point arithmetic:

```python
>>> 2.32 * 3 == 6.96
False
>>> 2.32 * 3
6.959999999999999  # Not ideal for financial calculations!
```

Dinero makes it simple and safe:

```python
>>> from dinero import Dinero
>>> from dinero.currencies import USD
>>>
>>> price = Dinero("2.32", USD)  # Use strings for maximum precision
>>> total = price * 3
>>> print(total.format(symbol=True))  # "$6.96"
>>> total == Dinero("6.96", USD)
True
```

## Quick Start

### Installation

```bash
pip install dinero
```

### Basic Usage

1. Create and Format Money:
```python
from dinero import Dinero
from dinero.currencies import USD, EUR

# Create monetary values
price = Dinero("99.99", USD)
discount = Dinero("10.00", USD)

# Format output
print(price.format(symbol=True, currency=True))  # "$99.99 USD"
```

2. Perform Currency-Safe Calculations:
```python
# Basic arithmetic
total = price - discount  # Dinero("89.99", USD)

# Safe currency handling
euro_price = Dinero("89.99", EUR)
try:
    total = price + euro_price  # Raises DifferentCurrencyError
except DifferentCurrencyError:
    print("Cannot add different currencies!")
```

3. Use Financial Tools:
```python
from dinero.tools import calculate_vat_portion, calculate_compound_interest

# Calculate VAT
vat = calculate_vat_portion(price, 20)  # 20% VAT
print(vat.format(symbol=True))  # "$20.00"

# Calculate compound interest
investment = Dinero("10000", USD)
future_value = calculate_compound_interest(
    principal=investment,
    interest_rate=5,  # 5% annual rate
    duration=10,      # 10 years
    compound_frequency=12  # Monthly compounding
)
```

4. Compare Monetary Values:
```python
from dinero.currencies import USD

price1 = Dinero("99.99", USD)
price2 = Dinero("89.99", USD)

# Using comparison operators
price1 > price2    # True - first price is higher

# Using methods for more explicit code
price1.eq(price2)  # False - prices are not equal
price2.lt(price1)  # True - price2 is less than price1
```

5. Convert Between Currencies:
```python
from dinero.currencies import USD, EUR, JPY

# Convert $100 USD to Euros with exchange rate 0.85
usd_price = Dinero("100.00", USD)
eur_price = usd_price.convert("0.85", EUR)
eur_price.format(symbol=True)  # "€85.00"

# Convert to Japanese Yen
jpy_price = usd_price.convert("110.50", JPY)
jpy_price.format(symbol=True, currency=True)  # "¥11,050 JPY"
```

## Features

### Type-Safe Currency Operations

```python
# Arithmetic operations
total = price + shipping
monthly = rent * 12
unit_cost = total_cost / quantity

# Method chaining for complex calculations
final_price = (
    Dinero("100.00", USD)
    .multiply(1.20)  # Add 20% markup
    .subtract("5.00")  # Apply discount
)
```

### Comparison Operators

```python
# Direct comparison operators
price1 < price2            # Less than -> returns True/False
price1 <= price2           # Less than or equal -> returns True/False
price1 > price2            # Greater than -> returns True/False
price1 >= price2           # Greater than or equal -> returns True/False
price1 == price2           # Equal -> returns True/False

# Method-based comparisons
price1.lt(price2)   # Less than -> returns True/False
price1.lte(price2)  # Less than or equal -> returns True/False
price1.gt(price2)   # Greater than -> returns True/False
price1.gte(price2)  # Greater than or equal -> returns True/False
price1.eq(price2)   # Equal -> returns True/False
```

### Currency Conversion

```python
from dinero.currencies import USD, EUR, CLP

# Convert USD to EUR with an exchange rate of 0.85
usd_amount = Dinero("100", USD)
eur_amount = usd_amount.convert("0.85", EUR)
eur_amount.format(symbol=True)  # "€85.00"

# Convert USD to CLP (which has 0 decimal places)
clp_amount = usd_amount.convert(750, CLP)
clp_amount.format(currency=True)  # "75,000 CLP"

# Function-based conversion
from dinero.tools.conversion import convert
jpy_amount = convert(usd_amount, "110.25", JPY)
jpy_amount.format()  # "11,050"
```

### Currency Support

- Access over 100 pre-defined ISO 4217 currencies:
```python
from dinero.currencies import USD, EUR, GBP, JPY, BTC

# Each currency knows its symbol and decimal places
amount = Dinero("42.42", EUR)
print(amount.format(symbol=True))  # "€42.42"
```

- Create custom currencies:
```python
from dinero.types import Currency

GOLD = {
    "code": "XAU",
    "base": 10,
    "exponent": 4,  # 4 decimal places
    "symbol": "Au"
}

gold_price = Dinero("1842.5930", GOLD)
print(gold_price.format(symbol=True))  # "Au1,842.5930"
```

## Best Practices

1. **Use String Inputs**: Avoid float precision issues by using strings:
```python
# Good ✅
amount = Dinero("42.42", USD)

# Avoid ❌
amount = Dinero(42.42, USD)  # Potential precision loss
```

2. **Handle Currency Mismatches**: Always validate currency compatibility:
```python
# Good ✅
try:
    total = usd_price + eur_price
except DifferentCurrencyError:
    # Convert currencies or handle error
```

3. **Format for Display**: Use appropriate formatting options:
```python
# Full format with symbol and code
price.format(symbol=True, currency=True)  # "$42.42 USD"

# Just the number
price.format()  # "42.42"
```

For more detailed information and advanced features, check out our [comprehensive documentation](https://wilfredinni.github.io/dinero/).

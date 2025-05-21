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

This project is inspired by the excellent [dinero.js](https://github.com/dinerojs/dinero.js) library.

## Key Features

- 🎯 **Precise Calculations**: Built on Python's `Decimal` type for exact monetary computations.
- 🔒 **Type Safety**: Full type hint support and runtime validation.
- 🌍 **Currency Support**: Over 100 currencies following ISO 4217 standards (see [Currencies](currencies.md)).
- 🧮 **Financial Tools**: Built-in support for VAT, interest calculations, markup, and more (see [Tools](tools.md)).
- 🔄 **Immutable Objects**: Thread-safe with predictable behavior.
- 💪 **Modern Python**: Type hints, clean API, and comprehensive test coverage.

## Why Dinero?

Working with money in Python can be tricky due to floating-point arithmetic:

```python
>>> 2.32 * 3 == 6.96
False
>>> 2.32 * 3
6.959999999999999  # Not ideal for financial calculations!
```

You can read [How to Count Money Exactly in Python](https://learnpython.com/blog/count-money-python/) to get a better idea.

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

A `Dinero` object represents a specific monetary value. It comes with methods for creating, parsing, manipulating, testing, and formatting.

## Quick Start

For more detailed examples and explanations, see the [Getting Started](started.md) guide.

### Installation

```bash
pip install dinero
```

### Basic Usage

1.  **Create and Format Money**:
    ```python
    from dinero import Dinero
    from dinero.currencies import USD, EUR

    # Create monetary values
    price = Dinero("99.99", USD)
    discount = Dinero("10.00", USD)

    # Format output
    print(price.format(symbol=True, currency=True))  # "$99.99 USD"
    ```

2.  **Perform Currency-Safe Calculations**:
    ```python
    # Basic arithmetic (see more on [Operations](started.md#operations))
    total = price - discount  # Dinero("89.99", USD)
    print(total.format(symbol=True)) # "$89.99"

    # Safe currency handling
    from dinero.exceptions import DifferentCurrencyError # Import for the try-except block
    euro_price = Dinero("89.99", EUR)
    try:
        # total_mixed = price + euro_price  # This would raise DifferentCurrencyError
        # To make example runnable and demonstrate same currency operations:
        another_usd_price = Dinero("10.01", USD)
        new_total = price + another_usd_price
        print(new_total.format(symbol=True)) # "$110.00"

    except DifferentCurrencyError:
        print("Cannot add different currencies directly!")
    ```

3.  **Use Financial Tools**:
    ```python
    from dinero import Dinero
    from dinero.currencies import USD
    from dinero.tools import calculate_vat_portion, calculate_compound_interest

    # Calculate VAT (see more in [Tools](tools.md))
    # Example: Calculate 20% VAT from a gross price of $120.00
    gross_price = Dinero("120.00", USD)
    vat_on_gross = calculate_vat_portion(gross_price, 20) # 20% VAT rate
    print(f"VAT portion from {gross_price.format(symbol=True)} at 20%: {vat_on_gross.format(symbol=True)}") # "$20.00"

    # Calculate compound interest (interest earned)
    investment = Dinero("10000", USD)
    # The function calculate_compound_interest returns the interest earned.
    interest_earned = calculate_compound_interest(
        principal=investment,
        interest_rate=5,  # 5% annual rate
        duration=10,      # 10 years
        compound_frequency=12  # Monthly compounding
    )
    # Output based on Decimal calculation (actual Dinero output might vary slightly due to internal precision)
    print(f"Interest earned over 10 years: {interest_earned.format(symbol=True, currency=True)}") # "$6,470.09 USD (Interest Earned)"
    ```

4.  **Compare Monetary Values**:
    ```python
    from dinero import Dinero
    from dinero.currencies import USD

    price1 = Dinero("99.99", USD)
    price2 = Dinero("89.99", USD)

    # Using comparison operators (see more on [Comparisons](started.md#comparisons))
    print(price1 > price2)    # True

    # Using methods for more explicit code
    print(price1.eq(price2))  # False
    print(price2.lt(price1))  # True
    ```

5.  **Convert Between Currencies**:
    ```python
    from dinero import Dinero
    from dinero.currencies import USD, EUR, JPY

    # Convert $100 USD to Euros with exchange rate 0.85
    usd_price = Dinero("100.00", USD)
    eur_price = usd_price.convert("0.85", EUR)
    print(eur_price.format(symbol=True))  # "€85.00"

    # Convert to Japanese Yen
    jpy_price = usd_price.convert("110.50", JPY)
    print(jpy_price.format(symbol=True, currency=True))  # "¥11,050 JPY"
    ```

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

amount = Dinero("100.40", USD) # Initialize with string for precision

## Best Practices

When working with Dinero, consider the following best practices for optimal precision and safety:

1.  **Use String Inputs for Amounts**: To avoid potential floating-point precision issues inherent in binary representations of decimals, it's highly recommended to initialize `Dinero` objects using string representations of amounts, especially when dealing with fractional values.

    ```python
    from dinero import Dinero
    from dinero.currencies import USD

    # Good ✅ - Preserves exact precision
    price_string = Dinero("19.99", USD)
    fee_string = Dinero("0.05", USD)

    # Avoid ❌ - Can lead to precision loss with certain floats
    # price_float = Dinero(19.99, USD) # e.g., 19.99 might be stored as 19.989999...
    # fee_float = Dinero(0.05, USD)   # e.g., 0.05 might be stored as 0.050000...
    ```
    Using strings ensures that the exact decimal value you provide is used.

2.  **Handle Currency Mismatches**: `Dinero` enforces that arithmetic operations like addition and subtraction are performed only between objects of the same currency. Attempting to operate on different currencies will raise a `DifferentCurrencyError`. Always ensure currency compatibility or convert amounts to a common currency before performing such operations.

    See the [Operations](#operations) section for an example of `DifferentCurrencyError` and how to handle it, and [Currency Conversion](#currency-conversion) for converting between currencies.

3.  **Format for Display**: `Dinero` objects have a powerful `format()` method to control how monetary values are displayed. Use this method to get string representations suitable for user interfaces or reports.

    For detailed information on formatting options, refer to the [Formatting](#formatting) section.
    ```python
    # Example:
    # formatted_price = price_string.format(symbol=True, currency=True) # "$19.99 USD"
    # print(formatted_price)
    ```

## Key Design Principles

Dinero is built with several core principles in mind to ensure reliability, safety, and ease of use in monetary calculations.

### Type Safety

Dinero extensively uses Python's type hints for both `Dinero` objects and `Currency` dictionaries. This offers several advantages:
-   **Early Error Detection**: Type hints allow static analysis tools (like MyPy) to catch potential type-related errors before runtime.
-   **Improved Code Clarity**: Explicit types make the codebase easier to understand and maintain.
-   **Enhanced Developer Experience**: IDEs can provide better autocompletion and suggestions.

For defining currency dictionaries with type safety, you can use `dinero.types.Currency`. An example is available in the [Type hints](#type-hints) subsection under "Custom Currencies".

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.types import Currency

# Dinero objects are fully typed
price: Dinero = Dinero("100", USD)

# Currency dictionaries can be typed too
# For example, when defining a custom currency:
gold_currency_def: Currency = {"code": "XAU", "base": 10, "exponent": 2, "symbol": "Gold"}
# gold_price: Dinero = Dinero("1500", gold_currency_def) # Example usage
```

### Runtime Validation

Beyond static type checking, Dinero performs runtime validations to prevent common errors in monetary operations:
-   **Currency Consistency**: Operations that combine amounts (like addition or subtraction) require the `Dinero` objects to have the same currency. Attempting to operate on different currencies will raise a `DifferentCurrencyError` (from `dinero.exceptions`), as shown in the [Operations](#operations) section.
-   **Input Validation**: Dinero objects validate input types for amounts and other critical parameters to ensure operations are performed correctly. For example, currency conversion rates must be provided in a format that can be accurately processed into a `Decimal`.

These runtime checks help catch errors that might not be visible to static analysis, ensuring data integrity during calculations.

### Immutability

`Dinero` objects are immutable. This means that once a `Dinero` object is created, its value cannot change. Any operation that appears to modify a `Dinero` object actually returns a new `Dinero` instance with the result of the operation.

Benefits of immutability include:
-   **Predictable State**: You can be confident that a `Dinero` object's value won't change unexpectedly after creation or being passed to other functions.
-   **Thread Safety**: Immutable objects are inherently thread-safe, simplifying development in multi-threaded applications.
-   **Easier Debugging**: When values don't change, it's simpler to trace program flow and reason about state.

```python
from dinero import Dinero
from dinero.currencies import USD

initial_price = Dinero("100.00", USD)
discount = Dinero("10.00", USD)

# Subtracting the discount creates a new Dinero object
final_price = initial_price - discount

# The original object remains unchanged
print(f"Initial price: {initial_price.format(symbol=True)}")  # $100.00
print(f"Final price: {final_price.format(symbol=True)}")    # $90.00

assert initial_price == Dinero("100.00", USD) # Value is the same
assert final_price == Dinero("90.00", USD)
assert id(initial_price) != id(final_price) # They are different objects
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
>>> from dinero import Dinero
>>> from dinero.currencies import USD
>>> d = Dinero("1234.56", USD)
>>> d.to_json()
'{"amount": "1234.56", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'
```

```python title="amount_with_format=True"
>>> from dinero import Dinero
>>> from dinero.currencies import USD
>>> d = Dinero("1234.56", USD)
>>> d.to_json(amount_with_format=True)
'{"amount": "1,234.56", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'
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

### Currency Conversion

You can convert between different currencies using the `convert` method:

```python title='Currency Conversion'
from dinero.currencies import USD, EUR, CLP

# Convert USD to EUR with an exchange rate of 0.85
usd_amount = Dinero("100", USD)
eur_amount = usd_amount.convert("0.85", EUR)
eur_amount.format(symbol=True)
'€85.00'

# Convert USD to CLP (which has 0 decimal places)
clp_amount = usd_amount.convert(750, CLP)
clp_amount.format(currency=True)
'75,000 CLP'
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
Dinero(1000, USD).eq(Dinero(1000, USD))
Dinero(1000, USD) == Dinero(1000, USD)
```

```python title='Less than'
Dinero(1000, USD).lt(Dinero(1000, USD))
Dinero(1000, USD) < Dinero(1000, USD)
```

```python title='Less than or equal'
Dinero(1000, USD).lte(Dinero(1000, USD))
Dinero(1000, USD) <= Dinero(1000, USD)
```

```python title='Greater than'
Dinero(1000, USD).gt(Dinero(1000, USD))
Dinero(1000, USD) > Dinero(1000, USD)
```

```python title='Greater than or equal'
Dinero(1000, USD).gte(Dinero(1000, USD))
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

Dinero give you access to some useful tools that allow you to perform common monetary calculations, like percentages, VAT, simple and compound interests, etc.

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

See all the available tools in the [tools](/dinero/tools/) section.

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

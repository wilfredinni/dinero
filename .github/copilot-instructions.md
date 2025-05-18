# GitHub Copilot Instructions for Dinero

This file provides guidance for GitHub Copilot when working with the Dinero library code.

## Core Principles

When suggesting code for the Dinero library:

1. Always use Python's `Decimal` type for internal monetary calculations
2. Maintain immutability - never modify existing Dinero instances
3. Ensure type safety through proper type hints and runtime validation
4. Follow ISO 4217 standards for currency handling
5. Preserve decimal precision based on currency specifications

## Code Patterns

### Creating Dinero Instances

```python
# CORRECT - Use strings for precise monetary values
amount = Dinero("42.42", USD)

# CORRECT - Use Decimal for precise values
from decimal import Decimal
amount = Dinero(Decimal("42.42"), USD)

# AVOID - Using float literals can lead to precision issues
amount = Dinero(42.42, USD)  # Not recommended
```

### Arithmetic Operations

```python
# CORRECT - Chain operations with proper type handling
result = price.multiply(quantity).subtract(discount)

# CORRECT - Compare only same-currency values
if price1.currency == price2.currency and price1.lt(price2):
    # Handle comparison
```

### Error Handling

```python
# CORRECT - Handle currency mismatches explicitly
try:
    total = price_usd.add(price_eur)  # Will raise InvalidOperationError
except InvalidOperationError:
    # Handle currency mismatch
```

## Project Structure Guidelines

### File Organization
- Place currency definitions in `currencies/` directory
- Core implementation files are prefixed with underscore (`_dinero.py`, `_operations.py`)
- Tests should mirror the structure of source files

### Naming Conventions
- Currency classes: Uppercase (USD, EUR, GBP)
- Private methods/functions: Prefixed with underscore
- Test files: Prefixed with `test_`

## Testing Requirements

When suggesting test code:

1. Use parametrized tests for different input types:
```python
@pytest.mark.parametrize(
    "amount,expected",
    [
        ("42.42", "42.42"),
        (Decimal("42.42"), "42.42"),
        (42, "42.00")
    ]
)
def test_amount_handling(amount, expected):
    assert Dinero(amount, USD).format() == expected
```

2. Include edge cases:
- Zero amounts
- Negative values
- Maximum/minimum currency-specific values
- Different decimal precisions

3. Test error conditions:
- Invalid currency combinations
- Invalid amount formats
- Invalid operation parameters

## Documentation Standards

When suggesting documentation:

1. Include docstrings with:
- Description of functionality
- Parameter types and descriptions
- Return value description
- Usage examples
- Possible exceptions

```python
def multiply(self, factor: int | float | str | Decimal) -> "Dinero":
    """Multiply a monetary value by a factor.

    Args:
        factor: The number to multiply by. Can be int, float, str, or Decimal.

    Returns:
        A new Dinero instance with the multiplied amount.

    Raises:
        InvalidOperationError: If the factor is invalid.

    Example:
        >>> price = Dinero("10.00", USD)
        >>> price.multiply(3)
        Dinero("30.00", USD)
    """
```

## Common Pitfalls to Avoid

1. Never use floating-point arithmetic directly for monetary calculations
2. Don't mix currencies in arithmetic operations without explicit conversion
3. Avoid mutable state in monetary calculations
4. Don't assume fixed decimal places - use currency-specific precision
5. Never round intermediate calculation results

## Integration Patterns

When working with external systems:

1. Use `to_dict()` and `to_json()` for serialization
2. Validate incoming monetary values before creating Dinero instances
3. Handle currency conversion explicitly
4. Use proper error handling for integration boundaries
5. Preserve precision during data transfer

## Performance Considerations

1. Reuse currency instances rather than creating new ones
2. Batch operations when possible
3. Validate inputs early to avoid unnecessary calculations
4. Use appropriate data structures for bulk operations
5. Consider memory usage with large collections of monetary values

## Security Guidelines

1. Validate all input amounts and currencies
2. Use secure serialization/deserialization methods
3. Handle overflow and underflow conditions
4. Protect against precision loss
5. Validate currency codes against ISO 4217 standards

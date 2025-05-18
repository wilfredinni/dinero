# Dinero Project Overview

## 1. Project Overview

### Core Purpose and Objectives
Dinero is a Python library designed to handle monetary calculations with precision and ease. Its primary objectives are:
- Provide exact monetary calculations without floating-point precision errors
- Offer an intuitive and clean API for handling monetary values
- Support multiple currencies using ISO 4217 standards
- Ensure immutability and type safety in monetary operations

### Main Features and Capabilities
- Precise decimal arithmetic for monetary calculations
- Currency formatting with symbols and codes
- Basic arithmetic operations (add, subtract, multiply, divide)
- Comparison operations
- JSON serialization and deserialization
- Type-safe operations with built-in validation
- Support for multiple currency representations

### Technology Stack and Dependencies
- **Core Dependencies:**
  - Python ≥ 3.10
  - typing-extensions ≥ 4.12.2
- **Development Tools:**
  - Poetry for dependency management
  - pytest for testing
  - mypy for type checking
  - Coverage.py for test coverage
- **Documentation:**
  - MkDocs with Material theme
  - MkDocstrings for Python documentation

### System Architecture Overview
The project follows a modular architecture with clear separation of concerns:
- Core money handling (`_dinero.py`)
- Operation implementations (`_operations.py`)
- Validation logic (`_validators.py`)
- Utility functions (`_utils.py`)
- Currency definitions (currencies/ module)
- Type definitions (`types.py`)

## 2. Key Components

### Class Structures and Inheritance Hierarchy
```
Operations (Base Class)
└── Dinero
    └── Core monetary operations implementation
```

### Public Interfaces and APIs
The `Dinero` class provides the following main interfaces:
- Constructor: `Dinero(amount, currency)`
- Formatting: `format(symbol=False, currency=False)`
- Arithmetic: `add()`, `subtract()`, `multiply()`, `divide()`
- Comparison: `equals_to()`, `less_than()`, `greater_than()`, etc.
- Serialization: `to_dict()`, `to_json()`

### Important Methods and Signatures
```python
class Dinero:
    def __init__(self, amount: int | float | str | Decimal, currency: Currency)
    def format(self, symbol: bool = False, currency: bool = False) -> str
    def add(self, other: 'Dinero') -> 'Dinero'
    def subtract(self, other: 'Dinero') -> 'Dinero'
    def multiply(self, factor: int | float | str | Decimal) -> 'Dinero'
    def divide(self, factor: int | float | str | Decimal) -> 'Dinero'
```

### Data Models and Schemas
- **Currency Type:**
  - Defined as a TypedDict with ISO 4217 properties
  - Includes code, decimals, and symbol information

## 3. Implementation Details

### Design Patterns
- **Immutable Value Objects:** All Dinero instances are immutable
- **Factory Pattern:** Currency constructors for different ISO currencies
- **Composition:** Separation of operations, validation, and core logic
- **Type-Safety:** Extensive use of Python's type hints and runtime validation

### Code Organization Principles
- Modular design with clear separation of concerns
- Private implementation modules prefixed with underscore
- Public API exposed through main package
- Currency implementations in separate modules
- Comprehensive test coverage for all components

### Notable Algorithms and Workflows
1. **Decimal Handling:**
   - Uses Python's Decimal for precise calculations
   - Automatic rounding to currency-specific decimal places
   - Validation of decimal precision and scale

2. **Currency Operations:**
   - Currency matching validation for arithmetic operations
   - Scale-aware calculations based on currency definitions
   - Proper rounding strategies for different currencies

### Configuration Settings
- Currency-specific decimal places
- Formatting options for symbols and codes
- Type validation settings
- Customizable through currency definitions

## 4. Usage Guidelines

### Common Use Cases
```python
# Basic monetary calculations
price = Dinero(2.32, USD)
quantity = 3
total = price.multiply(quantity)  # $6.96

# Currency formatting
price.format(symbol=True)  # "$2.32"
price.format(currency=True)  # "2.32 USD"

# Arithmetic operations
total = price1.add(price2)
discount = total.multiply(0.1)
```

### Best Practices
1. Always use string or Decimal inputs for maximum precision
2. Perform currency validation before operations
3. Use proper rounding methods for calculations
4. Handle currency mismatches explicitly
5. Validate amounts before creating Dinero instances

### Known Limitations
- Only supports ISO 4217 currencies
- No built-in currency conversion
- Operations require matching currencies
- No support for custom currencies

### Error Handling Patterns
- Type validation errors
- Currency mismatch errors
- Invalid operation errors
- Amount validation errors

## 5. Integration Points

### External Dependencies
- Minimal runtime dependencies
- Core Python decimal module
- Type hints support
- JSON serialization capabilities

### APIs and Service Interactions
- JSON serialization for API integration
- Dict conversion for data storage
- String formatting for display
- Type hints for IDE integration

### Event Handling
- Exception handling for invalid operations
- Validation events during instantiation
- Type checking during operations

### Data Flow Patterns
1. Input validation → Amount normalization → Operation execution → Result formatting
2. Currency validation → Operation validation → Calculation → New immutable instance
3. Serialization → External system integration → Deserialization

## 6. Testing Framework

### Test Structure
```
tests/
├── test_dinero.py      # Core functionality tests
├── test_operations.py  # Arithmetic operations tests
├── test_utils.py      # Utility function tests
└── test_validators.py # Validation logic tests
```

### Test Coverage Requirements
- High test coverage (>90%)
- Unit tests for all public APIs
- Integration tests for currency operations
- Edge case testing for numerical operations

### Mocking Strategies
- Currency definitions mocking
- Decimal operation mocking
- Error condition simulation
- Exchange rate scenario testing

### Common Test Patterns
1. Parametrized tests for different input types
2. Currency operation validation tests
3. Formatting and display tests
4. Error condition tests
5. Edge case numerical tests

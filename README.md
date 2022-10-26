# Dinero [alpha]

Dinero is a library for working with monetary values in Python.

```python
from dinero import Dinero
from dinero.currencies import CLP, USD

amount = Dinero(234342.3010, USD)
amount.raw_amount
amount.symbol
amount.code

formatted = amount.get_amount(symbol=True, currency=True)
print(formatted)
```

    $234,342.30 USD

```python
from dinero import Dinero
from dinero.currencies import CLP, USD

unit_price = Dinero(2.32, USD)
number_sold = 3
money_received = 6.96
if unit_price * number_sold == money_received:
    print('Accounts balanced')
else:
    raise ValueError('Accounts not balanced')
```

    Accounts balanced

## Operations

### Add

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("333.3", EUR)
total = amount.add(333.3)
print(total)
```

    666.60

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, EUR)

total = amount_1.add(amount_2)
print(total)
```

    666.60

```python
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", USD)
amount_2 = Dinero(333.3, USD)

total = amount_1 + amount_2
print(total)
```

    666.60

```python
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, EUR)
amount_3 = Dinero(333.3, EUR)

total = sum([amount_1, amount_2, amount_3])
print(total)
```

    999.90

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD
from dinero.exceptions import DifferentCurrencyError

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, USD)

try:
    amount_1.add(amount_2)
    amount_1 + amount_2
    sum([amount_1, amount_2])
except DifferentCurrencyError:
    print('Can not operate with different currencies')
```

    Can not operate with different currencies

### Subtract

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20.20", EUR)
total = amount.subtract('10.20')
print(total)
```

    10.00

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.20", EUR)
amount_2 = Dinero("10.20", EUR)
total = amount_1.subtract(amount_2)
print(total)
```

    10.00

```python
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("20.20", EUR)
amount_2 = Dinero("10.20", EUR)
total = amount_1 - amount_2
print(total)
```

    10.00

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD
from dinero.exceptions import DifferentCurrencyError

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, USD)

try:
    amount_1.subtract(amount_2)
    amount_1 - amount_2
except DifferentCurrencyError:
    print('Can not operate with different currencies')
```

    Can not operate with different currencies

### Multiply

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20", EUR)
total = amount.multiply(2)
print(total)
```

    40.00

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1.multiply(amount_2)
print(total)
```

    40.00

```python
from dinero import Dinero
from dinero.currencies import EUR, CLP

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1 * amount_2
print(total)
```

    40.00

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("20.00", USD)
total = amount * 2.9
print(total)
```

    58.00

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD
from dinero.exceptions import DifferentCurrencyError

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, USD)

try:
    amount_1.multiply(amount_2)
    amount_1 * amount_2
except DifferentCurrencyError:
    print('Can not operate with different currencies')
```

    Can not operate with different currencies

### Divide

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20", EUR)
total = amount.divide(2)
print(total)
```

    10.00

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1.divide(amount_2)
print(total)
```

    10.00

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1 / amount_2
print(total)
```

    10.00

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20", EUR)
total = amount / 2
print(total)
```

    10.00

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD
from dinero.exceptions import DifferentCurrencyError

amount_1 = Dinero("20", EUR)
amount_2 = Dinero(2, USD)

try:
    amount_1.divide(amount_2)
    amount_1 / amount_2
except DifferentCurrencyError:
    print("Can not operate with different currencies")
```

    Can not operate with different currencies

### Operations

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("333.2", EUR)
amount_2 = Dinero(333.3, EUR)
amount_3 = Dinero(333.4, EUR)

highest = max([amount_1, amount_2, amount_3])
lowest = min([amount_1, amount_2, amount_3])

print(highest)
print(lowest)
```

    333.40
    333.20

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("333.2", EUR)
amount_2 = Dinero(333.3, EUR)

# less than
amount_1.less_than(amount_2)
amount_1.less_than(333.3)
amount_1 < amount_2
amount_1 < 333.3

# less than or equal
amount_1.less_than_or_equal(amount_2)
amount_1.less_than_or_equal(333.3)
amount_1 <= amount_2
amount_1 <= 333.3

# greater than
amount_1.greater_than(amount_2)
amount_1.greater_than(333.3)
amount_1 < amount_2
amount_1 < 333.3

# greater than or equal
amount_1.greater_than_or_equal(amount_2)
amount_1.greater_than_or_equal(333.3)
amount_1 > amount_2
amount_1 > 333.3

# equals
amount_3 = Dinero(333.2, EUR)
amount_1.equals_to(amount_3)
amount_1.equals_to(333.2)
amount_1 == amount_3
amount_1 == 333.2
```

    True

## to_dict

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("3333.259", USD)
amount.to_dict(amount_with_format=False)
```

    {'amount': '3333.26',
     'currency': {'code': 'USD', 'base': 10, 'exponent': 2, 'symbol': '$'}}

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("3333.259", USD)
amount.to_dict(amount_with_format=True)
```

    {'amount': '3,333.26',
     'currency': {'code': 'USD', 'base': 10, 'exponent': 2, 'symbol': '$'}}

## to_json

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("3333.2", USD)
amount.to_json(amount_with_format=False)
```

    '{"amount": "3333.20", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("3333.2", USD)
amount.to_json(amount_with_format=True)
```

    '{"amount": "3,333.20", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'

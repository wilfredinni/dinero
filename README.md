# Dinero [alpha]

Dinero is a WIP library for working with monetary values in Python.

## Install

```
pip install dinero
```

## Example

```python
from dinero import Dinero
from dinero.currencies import USD

unit_price = Dinero(2.32, USD)
money_received = Dinero(6.96, USD)
number_sold = 3
if unit_price * number_sold == money_received:
    print('Accounts balanced')
    print(money_received.format_amount(symbol=True, currency=True))
else:
    raise ValueError('Accounts not balanced')
```

```
Accounts balanced
$6.96 USD
```

## Documentation

[Documentation](https://wilfredinni.github.io/dinero/)

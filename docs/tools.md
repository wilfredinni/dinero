
# Tools

This module provides a collection of tools that can be used to perform common monetary calculations.

## Calculate VAT

This function calculates the VAT amount of a given monetary value. It takes two arguments: the monetary value as a Dinero object and the VAT percentage.

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_vat

amount = Dinero(100, USD)
vat_amount = calculate_vat(
    amount=amount,
    vat_rate=7.25,
)
vat_amount.format(symbol=True, currency=True)
'$6.76 USD'
```

## Calculate Percentage

This function calculates the percentage of a given monetary value. It takes two arguments: the monetary value as a Dinero object and the percentage.

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_percentage

amount = Dinero("3000", USD)
vat_amount = calculate_percentage(
    amount=amount,
    percentage=15,
)
vat_amount.format(symbol=True, currency=True)
'$450.00 USD'
```

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
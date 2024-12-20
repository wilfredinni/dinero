# Tools

This module provides a collection of tools that can be used to perform common monetary calculations.

## Calculate VAT

This function calculates the VAT amount of a given monetary value. It takes two arguments:

- **amount**: The amount to calculate the VAT of
- **vat_rate**: The VAT rate as a percentage

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

This function calculates the percentage of a given monetary value. It takes two arguments:

- **amount**: The amount to calculate the percentage of
- **percentage**: The percentage to calculate

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

## Calculate Simple Interest

This function calculates the simple interest of a given monetary value. It takes three arguments: 

- **principal**: The principal amount of the loan as a Dinero object
- **interest_rate**: The annual interest rate
- **duration**: The duration of the loan in years

Uses the formula `I = P * r * t`

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_simple_interest

amount = Dinero(1000, USD)
interest_amount = calculate_simple_interest(
    principal=amount,
    interest_rate=5,
    duration=2,
)
interest_amount.format(symbol=True, currency=True)
'$100.00 USD'
```

## Calculate Compound Interest

This function calculates the compound interest of a given monetary value. It takes four arguments:

 - **principal**: The monetary value as a Dinero object
 - **interest_rate**: The annual interest rate as a decimal
 - **duration**: The duration of the loan in years
 - **compound_frequency**: The number of times interest is compounded per year

Uses the formula `A = P(1 + r/n)^(nt)`

Example:


```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_compound_interest

principal = Dinero("2000", USD)
total_interest = calculate_compound_interest(
    principal=principal,
    interest_rate=5,
    duration=10,
    compound_frequency=12,
)
total_interest.format(symbol=True, currency=True)
'$1,294.02 USD'
```

## Calculate Markup

Calculates the markup of a given Dinero object:

- **cost**: The monetary value as a Dinero object
- **markup**: The percentage to calculate

Example:

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_markup

amount = Dinero("1000", USD)
vat_amount = calculate_markup(
    amount=amount,
    percentage=15,
)
vat_amount.format(symbol=True, currency=True)
'$1,150.00 USD'
```
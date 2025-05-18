## VAT Calculations

The library provides three functions for working with VAT (Value Added Tax):

### Calculate Net Amount

Extracts the net amount (excluding VAT) from a gross amount (including VAT):

- **amount**: The gross amount (including VAT)
- **vat_rate**: The VAT rate as a percentage

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools.vat import calculate_net_amount

gross_amount = Dinero(120, USD)  # Amount including 20% VAT
net_amount = calculate_net_amount(gross_amount, 20)
net_amount.format(symbol=True, currency=True)
'$100.00 USD'
```

### Calculate VAT Portion

Extracts just the VAT amount from a gross amount:

- **amount**: The gross amount (including VAT)
- **vat_rate**: The VAT rate as a percentage

```python
from dinero.tools.vat import calculate_vat_portion

gross_amount = Dinero(120, USD)  # Amount including 20% VAT
vat = calculate_vat_portion(gross_amount, 20)
vat.format(symbol=True, currency=True)
'$20.00 USD'
```

### Calculate Gross Amount

Adds VAT to a net amount to get the gross amount:

- **amount**: The net amount (excluding VAT)
- **vat_rate**: The VAT rate as a percentage

```python
from dinero.tools.vat import calculate_gross_amount

net_amount = Dinero(100, USD)  # Amount without VAT
gross_amount = calculate_gross_amount(net_amount, 20)
gross_amount.format(symbol=True, currency=True)
'$120.00 USD'
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

## Markup Calculations

The library provides three functions for working with markups:

### Calculate Base Amount

Extracts the base amount (excluding markup) from a final amount (including markup):

- **amount**: The final amount (including markup)
- **markup_rate**: The markup rate as a percentage

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools import calculate_base_amount

final_amount = Dinero(115, USD)  # Amount including 15% markup
base_amount = calculate_base_amount(final_amount, 15)
base_amount.format(symbol=True, currency=True)
'$100.00 USD'
```

### Calculate Markup Portion

Extracts just the markup amount from a final amount:

- **amount**: The final amount (including markup)
- **markup_rate**: The markup rate as a percentage

```python
from dinero.tools import calculate_markup_portion

final_amount = Dinero(115, USD)  # Amount including 15% markup
markup = calculate_markup_portion(final_amount, 15)
markup.format(symbol=True, currency=True)
'$15.00 USD'
```

### Calculate Marked Up Amount

Adds markup to a base amount to get the final amount:

- **amount**: The base amount (excluding markup)
- **markup_rate**: The markup rate as a percentage

```python
from dinero.tools import calculate_marked_up_amount

base_amount = Dinero(100, USD)  # Amount without markup
final_amount = calculate_marked_up_amount(base_amount, 15)
final_amount.format(symbol=True, currency=True)
'$115.00 USD'
```
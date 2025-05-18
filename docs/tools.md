## Currency Conversion

The library provides functionality to convert Dinero objects between different currencies using specified exchange rates:

### Convert

Converts a Dinero object to a different currency using the specified exchange rate. This can be used as either a method on Dinero objects or as a standalone function:

- **exchange_rate**: The exchange rate to use for conversion (as a string or float)
- **currency**: The target currency to convert to (a Currency object)

#### Method Usage

```python
from dinero import Dinero
from dinero.currencies import USD, EUR, CLP

# Convert USD to EUR with an exchange rate of 0.85
usd_amount = Dinero("100", USD)
eur_amount = usd_amount.convert("0.85", EUR)
eur_amount.format(symbol=True, currency=True)
'€85.00 EUR'

# Convert USD to CLP with an exchange rate of 750
clp_amount = usd_amount.convert(750, CLP)
clp_amount.format(currency=True)
'75,000 CLP'
```

#### Function Usage

```python
from dinero import Dinero
from dinero.currencies import USD, EUR
from dinero.tools.conversion import convert

usd_amount = Dinero("100", USD)
eur_amount = convert(usd_amount, "0.85", EUR)
eur_amount.format(symbol=True, currency=True)
'€85.00 EUR'
```

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

## Interest Calculations

The library provides tools for calculating both simple and compound interest on monetary amounts. All calculations are handled using the Dinero class to ensure precision in financial computations.

### Calculate Simple Interest

This function calculates the simple interest earned on a principal amount over time. Uses the formula:

```
I = P * r * t
```

where:
- I is the interest earned
- P is the principal amount
- r is the annual interest rate (as a percentage)
- t is the time in years

Arguments:
- **principal**: The principal amount as a Dinero object
- **interest_rate**: The annual interest rate as a percentage (e.g., 5 for 5%)
- **duration**: The time period in years

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools.interest import calculate_simple_interest

principal = Dinero(1000, USD)
interest = calculate_simple_interest(
    principal=principal,
    interest_rate=5,  # 5%
    duration=2,       # 2 years
)
interest.format(symbol=True, currency=True)
'$100.00 USD'  # 1000 * 0.05 * 2 = 100
```

### Calculate Compound Interest

This function calculates compound interest, where interest is earned not only on the principal but also on accumulated interest from previous periods. Uses the formula:

```
A = P * (1 + r/n)^(n*t)
Interest = A - P
```

where:
- A is the final amount
- P is the principal amount
- r is the annual interest rate (as a percentage)
- n is the number of times interest is compounded per year
- t is the time in years

Arguments:
- **principal**: The principal amount as a Dinero object
- **interest_rate**: The annual interest rate as a percentage (e.g., 5 for 5%)
- **duration**: The time period in years
- **compound_frequency**: Number of times interest is compounded per year (e.g., 12 for monthly)

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools.interest import calculate_compound_interest

principal = Dinero("2000", USD)
interest = calculate_compound_interest(
    principal=principal,
    interest_rate=5,        # 5%
    duration=10,            # 10 years
    compound_frequency=12,  # Compounded monthly
)
interest.format(symbol=True, currency=True)
'$1,294.02 USD'  # Total interest earned over 10 years
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
from dinero.tools.markup import calculate_base_amount

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
from dinero.tools.markup import calculate_markup_portion

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
from dinero.tools.markup import calculate_marked_up_amount

base_amount = Dinero(100, USD)  # Amount without markup
final_amount = calculate_marked_up_amount(base_amount, 15)
final_amount.format(symbol=True, currency=True)
'$115.00 USD'
```

## Margin Calculations

The library provides three functions for working with profit margins. Unlike markup which is calculated from the cost price, margin is calculated as a percentage of the selling price.

### Calculate Cost Amount

Extracts the cost amount from a selling price and margin rate:

- **amount**: The selling price (including margin)
- **margin_rate**: The margin rate as a percentage of selling price

```python
from dinero import Dinero
from dinero.currencies import USD
from dinero.tools.margin import calculate_cost_amount

selling_price = Dinero(100, USD)  # Amount including 20% margin
cost_amount = calculate_cost_amount(selling_price, 20)
cost_amount.format(symbol=True, currency=True)
'$80.00 USD'
```

### Calculate Margin Portion

Extracts just the margin amount from a selling price:

- **amount**: The selling price (including margin)
- **margin_rate**: The margin rate as a percentage of selling price

```python
from dinero.tools.margin import calculate_margin_portion

selling_price = Dinero(100, USD)  # Amount including 20% margin
margin = calculate_margin_portion(selling_price, 20)
margin.format(symbol=True, currency=True)
'$20.00 USD'
```

### Calculate Selling Price

Calculates the selling price from a cost amount and desired margin rate:

- **amount**: The cost amount (excluding margin)
- **margin_rate**: The desired margin rate as a percentage of selling price

```python
from dinero.tools.margin import calculate_selling_price

cost_amount = Dinero(80, USD)  # Cost amount before margin
selling_price = calculate_selling_price(cost_amount, 20)
selling_price.format(symbol=True, currency=True)
'$100.00 USD'
```
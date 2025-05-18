"""
Margin is a pricing strategy where the selling price is determined by the desired profit
margin as a percentage of the selling price (unlike markup which is based on cost).

Example calculation:
  Selling price:    $100
  Margin rate:       20%
  Margin amount:     $20 (20% of selling price)
  Cost price:       $80 (selling price - margin)

Margin vs Markup:
- Margin percentage is calculated from the selling price
- Markup percentage is calculated from the cost price
- Example: A 33.33% margin equals a 50% markup

Common uses:
- Retail pricing strategies
- Profit analysis
- Sales performance metrics
- Business valuation
- Financial planning
"""

from dinero import Dinero

from ._validators import ToolValidators


def calculate_cost_amount(amount: Dinero, margin_rate: int | float) -> Dinero:
    """
    Calculates the cost amount from a selling price and margin rate.

    Args:
        amount (Dinero): The selling price (including margin).
        margin_rate (int | float): The margin rate as a percentage of selling price.

    Returns:
        Dinero: The cost amount.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the margin_rate argument is not a number
        ValueError: If the margin_rate argument is negative or >= 100

    Examples:
        >>> selling_price = Dinero(100, USD)  # Amount including 20% margin
        >>> cost_amount = calculate_cost_amount(selling_price, 20)
        >>> cost_amount.format(symbol=True, currency=True)
        '$80.00 USD'
    """
    validate = ToolValidators()
    validate.margin_inputs(amount, margin_rate)
    cost_multiplier = 1 - (margin_rate / 100)
    return amount * cost_multiplier


def calculate_margin_portion(amount: Dinero, margin_rate: int | float) -> Dinero:
    """
    Calculates the margin portion from a selling price.

    Args:
        amount (Dinero): The selling price (including margin).
        margin_rate (int | float): The margin rate as a percentage of selling price.

    Returns:
        Dinero: The margin portion.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the margin_rate argument is not a number
        ValueError: If the margin_rate argument is negative or >= 100

    Examples:
        >>> selling_price = Dinero(100, USD)  # Amount including 20% margin
        >>> margin = calculate_margin_portion(selling_price, 20)
        >>> margin.format(symbol=True, currency=True)
        '$20.00 USD'
    """
    validate = ToolValidators()
    validate.margin_inputs(amount, margin_rate)
    cost_amount = calculate_cost_amount(amount, margin_rate)
    return amount - cost_amount


def calculate_selling_price(amount: Dinero, margin_rate: int | float) -> Dinero:
    """
    Calculates the selling price from a cost amount and desired margin rate.

    Args:
        amount (Dinero): The cost amount (excluding margin).
        margin_rate (int | float): The desired margin rate as a percentage selling price.

    Returns:
        Dinero: The selling price (including margin).

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the margin_rate argument is not a number
        ValueError: If the margin_rate argument is negative or >= 100

    Examples:
        >>> cost_amount = Dinero(80, USD)  # Cost amount before margin
        >>> selling_price = calculate_selling_price(cost_amount, 20)
        >>> selling_price.format(symbol=True, currency=True)
        '$100.00 USD'
    """
    validate = ToolValidators()
    validate.margin_inputs(amount, margin_rate)
    selling_price_multiplier = 1 / (1 - (margin_rate / 100))
    return amount * selling_price_multiplier

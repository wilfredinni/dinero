"""
Markup is a common pricing strategy where a percentage is added to the base cost of
a product to determine its selling price. The markup percentage represents the amount
added on top of the base cost to cover overhead expenses and generate profit.

Example calculation:
  Base cost:        $100
  Markup rate:       15%
  Markup amount:    $15 (15% of base)
  Final price:     $115 (base + markup)

Markup vs Margin:
- Markup percentage is calculated from the cost price
- Margin percentage is calculated from the selling price
- Example: A 50% markup equals a 33.33% margin

Common uses:
- Retail pricing
- Construction estimates
- Manufacturing costs
- Wholesale pricing
- Service pricing
"""

from dinero import Dinero

from ._validators import ToolValidators


def calculate_base_amount(amount: Dinero, markup_rate: int | float) -> Dinero:
    """
    Calculates the base amount (excluding markup) from a final amount (including markup).

    Args:
        amount (Dinero): The final amount (including markup).
        markup_rate (int | float): The markup rate as a percentage.

    Returns:
        Dinero: The base amount (excluding markup).

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the markup_rate argument is not a number
        ValueError: If the markup_rate argument is negative

    Examples:
        >>> final_amount = Dinero(115, USD)  # Amount including 15% markup
        >>> base_amount = calculate_base_amount(final_amount, 15)
        >>> base_amount.format(symbol=True, currency=True)
        '$100.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, markup_rate)  # We can reuse VAT validation
    divisor = 1 + (markup_rate / 100)
    return amount / divisor


def calculate_markup_portion(amount: Dinero, markup_rate: int | float) -> Dinero:
    """
    Calculates the markup portion from a final amount (including markup).

    Args:
        amount (Dinero): The final amount (including markup).
        markup_rate (int | float): The markup rate as a percentage.

    Returns:
        Dinero: The markup portion.

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the markup_rate argument is not a number
        ValueError: If the markup_rate argument is negative

    Examples:
        >>> final_amount = Dinero(115, USD)  # Amount including 15% markup
        >>> markup = calculate_markup_portion(final_amount, 15)
        >>> markup.format(symbol=True, currency=True)
        '$15.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, markup_rate)  # We can reuse VAT validation
    base_amount = calculate_base_amount(amount, markup_rate)
    return amount - base_amount


def calculate_marked_up_amount(amount: Dinero, markup_rate: int | float) -> Dinero:
    """
    Calculates the final amount (including markup) from a base amount.

    Args:
        amount (Dinero): The base amount (excluding markup).
        markup_rate (int | float): The markup rate as a percentage.

    Returns:
        Dinero: The final amount (including markup).

    Raises:
        InvalidOperationError: If the amount is not a Dinero object
        TypeError: If the markup_rate argument is not a number
        ValueError: If the markup_rate argument is negative

    Examples:
        >>> base_amount = Dinero(100, USD)  # Amount without markup
        >>> final_amount = calculate_marked_up_amount(base_amount, 15)
        >>> final_amount.format(symbol=True, currency=True)
        '$115.00 USD'
    """
    validate = ToolValidators()
    validate.vat_inputs(amount, markup_rate)  # We can reuse VAT validation
    markup_multiplier = 1 + (markup_rate / 100)
    return amount * markup_multiplier

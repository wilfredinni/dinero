"""Tests for margin calculations."""

import pytest

from dinero import Dinero
from dinero.currencies import USD
from dinero.exceptions import InvalidOperationError
from dinero.tools.margin import (
    calculate_cost_amount,
    calculate_margin_portion,
    calculate_selling_price,
)


def test_calculate_cost_amount():
    """Test calculating cost amount from selling price."""
    # Test with 20% margin ($100 selling price = $80 cost)
    selling_price = Dinero("100.00", USD)
    cost = calculate_cost_amount(selling_price, 20)
    assert cost == Dinero("80.00", USD)

    # Test with 0% margin (cost equals selling price)
    selling_price = Dinero("100.00", USD)
    cost = calculate_cost_amount(selling_price, 0)
    assert cost == Dinero("100.00", USD)


def test_calculate_margin_portion():
    """Test calculating margin portion from selling price."""
    # Test with 20% margin ($100 selling price = $20 margin)
    selling_price = Dinero("100.00", USD)
    margin = calculate_margin_portion(selling_price, 20)
    assert margin == Dinero("20.00", USD)

    # Test with 0% margin (no margin)
    selling_price = Dinero("100.00", USD)
    margin = calculate_margin_portion(selling_price, 0)
    assert margin == Dinero("0.00", USD)


def test_calculate_selling_price():
    """Test calculating selling price from cost amount."""
    # Test with 20% margin ($80 cost = $100 selling price)
    cost = Dinero("80.00", USD)
    selling_price = calculate_selling_price(cost, 20)
    assert selling_price == Dinero("100.00", USD)

    # Test with 0% margin (selling price equals cost)
    cost = Dinero("100.00", USD)
    selling_price = calculate_selling_price(cost, 0)
    assert selling_price == Dinero("100.00", USD)


def test_invalid_inputs():
    """Test handling of invalid inputs."""
    amount = Dinero("100.00", USD)

    # Test invalid amount type
    with pytest.raises(InvalidOperationError):
        calculate_cost_amount(100, 20)  # type: ignore

    # Test invalid margin rate type
    with pytest.raises(TypeError):
        calculate_cost_amount(amount, "20")  # type: ignore

    # Test negative margin rate
    with pytest.raises(ValueError):
        calculate_cost_amount(amount, -20)

    # Test margin rate >= 100
    with pytest.raises(ValueError):
        calculate_cost_amount(amount, 100)

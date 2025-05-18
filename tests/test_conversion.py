"""
Test module for conversion functions.
"""

from decimal import Decimal

import pytest

from dinero import Dinero
from dinero.currencies import CLP, EUR, USD

# from dinero.exceptions import InvalidOperationError
from dinero.tools import convert


class TestConversion:
    """Tests for currency conversion functionality."""

    def test_convert_with_string_exchange_rate(self):
        """Test conversion with string exchange rate."""
        # Create a Dinero object in USD
        usd_amount = Dinero("100", USD)

        # Convert to EUR with string exchange rate
        eur_amount = usd_amount.convert("0.85", EUR)

        # Verify the conversion was successful
        assert isinstance(eur_amount, Dinero)
        assert eur_amount.currency == EUR
        assert eur_amount.raw_amount == Decimal("85.00")
        assert eur_amount.format() == "85.00"

    def test_convert_with_float_exchange_rate(self):
        """Test conversion with float exchange rate."""
        # Create a Dinero object in USD
        usd_amount = Dinero("100", USD)

        # Convert to EUR with float exchange rate
        eur_amount = usd_amount.convert(0.85, EUR)

        # Verify the conversion was successful
        assert isinstance(eur_amount, Dinero)
        assert eur_amount.currency == EUR
        assert eur_amount.raw_amount == Decimal("85.00")

    def test_convert_with_decimal_precision(self):
        """Test conversion with different decimal precision."""
        # Create a Dinero object in USD (2 decimal places)
        usd_amount = Dinero("100", USD)

        # Convert to CLP (0 decimal places)
        clp_amount = usd_amount.convert("750", CLP)

        # Verify the conversion respects the target currency's precision
        assert isinstance(clp_amount, Dinero)
        assert clp_amount.currency == CLP
        assert clp_amount.raw_amount == Decimal("75000")
        assert clp_amount.format() == "75,000"

    def test_convert_with_module_function(self):
        """Test conversion using the module function directly."""
        # Create a Dinero object in USD
        usd_amount = Dinero("100", USD)

        # Convert to EUR using the module function
        eur_amount = convert(usd_amount, "0.85", EUR)

        # Verify the conversion was successful
        assert isinstance(eur_amount, Dinero)
        assert eur_amount.currency == EUR
        assert eur_amount.raw_amount == Decimal("85.00")

    @pytest.mark.parametrize(
        "invalid_rate",
        [
            "invalid",  # Non-numeric string
            "-0.85",  # Negative rate
            "-1",  # Negative rate
            "0",  # Zero rate
            0,  # Zero rate as integer
            -0.5,  # Negative rate as float
        ],
    )
    def test_convert_with_invalid_exchange_rate(self, invalid_rate):
        """Test conversion with invalid exchange rates."""
        # Create a Dinero object in USD
        usd_amount = Dinero("100", USD)

        # Attempt to convert with invalid exchange rate
        with pytest.raises(ValueError):
            usd_amount.convert(invalid_rate, EUR)

    def test_convert_with_invalid_currency(self):
        """Test conversion with invalid currency."""
        # Create a Dinero object in USD
        usd_amount = Dinero("100", USD)

        # Attempt to convert with invalid currency
        with pytest.raises(TypeError):
            usd_amount.convert("0.85", "EUR")  # type: ignore

    def test_convert_with_non_dinero_object(self):
        """Test conversion with non-Dinero object."""
        # Attempt to convert with a non-Dinero object
        with pytest.raises(TypeError):
            convert("100", "0.85", EUR)  # type: ignore

    def test_convert_decimal_precision(self):
        """Test that conversion maintains appropriate decimal precision."""
        # Create a Dinero object in USD with a fractional amount
        usd_amount = Dinero("100.25", USD)

        # Convert to EUR with a rate that would result in a long decimal
        eur_amount = usd_amount.convert("0.8523", EUR)

        # Verify the conversion maintains proper precision based on currency
        assert isinstance(eur_amount, Dinero)
        assert eur_amount.currency == EUR

        # EUR has 2 decimal places, so the result should be rounded to 2 places
        # 100.25 * 0.8523 = 85.4433, which should round to 85.44
        assert eur_amount.raw_amount == Decimal("85.44")

from decimal import InvalidOperation


class DifferentCurrencyError(Exception):
    """Different currencies where used."""


class InvalidOperationError(InvalidOperation):
    """Dinero obj was compared to something that is not int, str, float, or Dinero."""

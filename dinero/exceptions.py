from decimal import InvalidOperation


class DifferentCurrencyError(Exception):
    """Different currencies where used."""


class InvalidOperationError(InvalidOperation):
    """An operation between unsupported types was executed."""

    operation_msg = "An operation between unsupported types was executed."
    comparison_msg = "You can only compare against other Dinero instances."

from decimal import Decimal, InvalidOperation

from .types import OperationType
from .exceptions import InvalidOperationError


class Validate:
    @staticmethod
    def validate_addition_subtraction_amount(amount: OperationType | object) -> None:
        """Validate that the amount passed to an addition or subtraction is of valid type.

        Args:
            amount (str, int, float, Decimal, Dinero)

        Raises:
            InvalidOperationError: An operation between unsupported types was executed.
        """
        from ._dinero import Dinero

        try:
            if not isinstance(amount, (int, float, str, Decimal, Dinero)):
                raise InvalidOperationError(InvalidOperationError.operation_msg)

        except (ValueError, InvalidOperation):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

    @staticmethod
    def validate_multiplication_division_amount(number: int | float | Decimal) -> None:
        """Validate that the number passed to a multiplication and division is of valid type.

        Args:
            amount (int, float, Decimal)

        Raises:
            InvalidOperationError: An operation between unsupported types was executed.
        """
        try:
            if not isinstance(number, (int, float, Decimal)):
                raise InvalidOperationError(InvalidOperationError.operation_msg)

        except (ValueError, InvalidOperation):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

    @staticmethod
    def validate_dinero_amount(amount: int | float | str | Decimal) -> None:
        """Validate that the amount passed to Dinero is of valid type

        Args:
            amount (str, int, float, Decimal, Dinero)

        Raises:
            InvalidOperationError: An operation between unsupported types was executed.
        """
        from ._dinero import Dinero

        try:
            if not isinstance(amount, (int, float, str, Decimal, Dinero)):
                raise InvalidOperationError(InvalidOperationError.operation_msg)

            Decimal(amount)

        except (ValueError, InvalidOperation):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

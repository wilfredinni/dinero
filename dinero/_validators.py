from decimal import Decimal, InvalidOperation

from .exceptions import InvalidOperationError
from .types import OperationType


class Validators:
    @staticmethod
    def addition_and_subtraction_amount(amount: OperationType | object) -> None:
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
    def multiplication_and_division_amount(number: int | float | Decimal) -> None:
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
    def dinero_amount(amount: int | float | str | Decimal) -> None:
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

    @staticmethod
    def comparison_amount(amount: object) -> None:
        from ._dinero import Dinero

        if not isinstance(amount, Dinero):
            raise InvalidOperationError(InvalidOperationError.comparison_msg)

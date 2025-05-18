from dinero import Dinero
from dinero.exceptions import InvalidOperationError


class ToolValidators:
    @staticmethod
    def percentage_inputs(amount: Dinero, percentage: int | float) -> None:
        if not isinstance(amount, Dinero):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

        if not isinstance(percentage, (int, float)):
            raise TypeError("The percentage argument must be a number.")

        if percentage < 0:
            raise ValueError("The percentage argument cannot be negative.")

    @staticmethod
    def vat_inputs(amount: Dinero, vat_rate: int | float) -> None:
        if not isinstance(amount, Dinero):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

        if not isinstance(vat_rate, (int, float)):
            raise TypeError("The vat_rate argument must be a number.")

        if vat_rate < 0:
            raise ValueError("The vat_rate argument cannot be negative.")

    @staticmethod
    def simple_interest_inputs(
        principal: Dinero, interest_rate: int | float, duration: int
    ) -> None:
        if not isinstance(principal, Dinero):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

        if not isinstance(interest_rate, (int, float)):
            raise TypeError("The interest rate must be a number.")

        if not isinstance(duration, int):
            raise TypeError("The duration must be an integer.")

        if interest_rate < 0:
            raise ValueError("The interest rate cannot be negative.")

        if duration < 0:
            raise ValueError("The duration cannot be negative.")

    @staticmethod
    def compound_interest_inputs(
        principal: Dinero, interest_rate: float, duration: int, compound_frequency: int
    ) -> None:
        if not isinstance(principal, Dinero):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

        if not isinstance(interest_rate, (float, int)) or interest_rate <= 0:
            raise ValueError("Interest rate must be a positive float.")

        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        if not isinstance(compound_frequency, int) or compound_frequency <= 0:
            raise ValueError("Compound frequency must be a positive integer.")

    @staticmethod
    def margin_inputs(amount: Dinero, margin_rate: int | float) -> None:
        """
        Validate margin calculation inputs.

        Args:
            amount (Dinero): The amount to perform margin calculations on.
            margin_rate (int | float): The margin rate as a percentage.

        Raises:
            InvalidOperationError: If amount is not a Dinero object
            TypeError: If margin_rate is not a number
            ValueError: If margin_rate is negative or >= 100
        """
        if not isinstance(amount, Dinero):
            raise InvalidOperationError(InvalidOperationError.operation_msg)

        if not isinstance(margin_rate, (int, float)):
            raise TypeError("The margin_rate argument must be a number.")

        if margin_rate < 0:
            raise ValueError("The margin_rate argument cannot be negative.")

        if margin_rate >= 100:
            raise ValueError("The margin_rate argument must be less than 100.")

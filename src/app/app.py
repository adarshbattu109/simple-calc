"""Class calling operations defined"""


from config.config import OPERATIONS


class CalcApp:
    """Class representing the application performing the operation requested"""

    operation: str
    operands: list

    def __init__(self, operation: str, operands: list) -> None:
        self.operation: str = operation
        self.operands: list = operands

    def get_result(self) -> int:
        """Method that call upon the call for given operation and returns the computed value

        Returns:
            int: Result of the operation
        """
        operation_object = OPERATIONS[self.operation]
        result = operation_object.compute_result(self.operands)
        return result

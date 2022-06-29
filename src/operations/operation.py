"""Module Housing all the operations that can be performed by Simple Calculator"""

from abc import ABC, abstractmethod


class Operation(ABC):
    """This is an abstract class representing structure for all operations"""
    @abstractmethod
    def compute_result(self, operands: list):
        """Method to evaluate result of operation"""


class AdditionOperation(Operation):
    """Class to perform addition operation"""

    def compute_result(self, operands: list) -> int:
        """Method to compute the sum of two numbers

        Returns:
            int: Sum of operands provided to the object during initialization
        """
        value: int = operands.pop()
        for operand in operands:
            value += operand
        return value


class SubtractionOperation(Operation):
    """Class to perform subtraction operation"""

    def compute_result(self, operands: list) -> int:
        """Method to compute the difference of two numbers

        Returns:
            int: difference of operands provided to the object during initialization
        """
        value: int = operands.pop()
        for operand in operands:
            value -= operand
        return value


class MulitplyOperation(Operation):
    """Class to perform multipliction operation"""

    def compute_result(self, operands: list) -> int:
        """Method to compute the multiplication of two numbers

        Returns:
            int: product of operands provided to the object during initialization
        """
        value: int = operands.pop()
        for operand in operands:
            value *= operand
        return value


class DivideOperation(Operation):
    """Class to perform division operation"""

    def compute_result(self, operands: list) -> int:
        """Method to compute the sum of two numbers

        Returns:
            int: Quotient of operands
        """
        quotient: int = operands.pop()

        try:
            for operand in operands:
                quotient /= operand
        except ZeroDivisionError:
            print("Exception caught while trying to divide by Zero")
            quotient = 0
        return quotient

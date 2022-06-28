"""This file stores all the configurations for the Simple Calculator"""

from operations.operation import Operation, addition, subtraction, mulitply, divide


OPERATIONS: dict[str, Operation] = {
    "1": addition(),
    "2": subtraction(),
    "3": mulitply(),
    "4": divide(),
}

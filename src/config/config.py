"""This file stores all the configurations for the Simple Calculator"""

from operations.operation import AdditionOperation
from operations.operation import SubtractionOperation
from operations.operation import MulitplyOperation
from operations.operation import DivideOperation


OPERATIONS = {
    "1": AdditionOperation(),
    "2": SubtractionOperation(), ,
    "3": MulitplyOperation(),
    "4": DivideOperation(),
}

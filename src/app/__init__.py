"""Client Facing User interfce"""

import os
import sys
from app.app import CalcApp


def user_interface() -> None:
    """Method to show Looping interface"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("This is a Simple Calculator\n\n")
        print("The following operations can be perfomed")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        operation = input("\n\nEnter your choice : ")

        if operation == "5":
            print("Thanks for Trying it out!!!")
            sys.exit(0)
        if operation not in ["1", "2", "3", "4"]:
            input("Invalid choice, Press any key to continue...")
            continue

        operand_one = input("Enter value for operand one : ")
        operand_two = input("Enter value for operand two : ")
        result = main(operation, [int(operand_one), int(operand_two)])
        print(f"The Result is : {result}")
        input("Press any key to continue... ")


def main(operation: str, operands: list) -> int:
    """Main method that creates the app class instance and calls compute

    Args:
        operation (str): Operation to determin Operation class
        operands (list): list of items to work on

    Returns:
        int: result of the computation
    """
    app_obj = CalcApp(operation=operation, operands=operands)
    result = app_obj.get_result()
    return result


if __name__ == "__main__":
    user_interface()

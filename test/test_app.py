"""Test module for testing main function"""

import unittest

from app import main


class TestMain(unittest.TestCase):
    """Class to encapsulate tests for main method"""

    def test_main_addition(self):
        """Method to test addition function"""
        expected = 20
        operands_list = [10, 10]
        actual = main("1", operands_list)
        assert actual == expected

    def test_main_subtraction(self):
        """Method to test subtraction function"""
        expected = 0
        operands_list = [10, 10]
        actual = main("2", operands_list)
        assert actual == expected

    def test_main_mulitply(self):
        """Method to test mulitpliction function"""
        expected = 100
        operands_list = [10, 10]
        actual = main("3", operands_list)
        assert actual == expected

    def test_main_divide(self):
        """Method to test division function"""
        expected = 1
        operands_list = [10, 10]
        actual = main("4", operands_list)
        assert actual == expected

    def test_main_divide_by_zero(self):
        """Method to test division function with Exception"""
        expected = 0
        operands_list = [0, 10]
        actual = main("4", operands_list)
        assert actual == expected


if __name__ == '__main__':
    unittest.main()

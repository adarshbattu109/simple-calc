import unittest

from app import main


class test_main(unittest.TestCase):
    def test_main_addition(self):
        expected = 20
        operands_list = [10, 10]
        actual = main("1", operands_list)
        assert actual == expected

    def test_main_subtraction(self):
        expected = 0
        operands_list = [10, 10]
        actual = main("2", operands_list)
        assert actual == expected

    def test_main_mulitply(self):
        expected = 100
        operands_list = [10, 10]
        actual = main("3", operands_list)
        assert actual == expected

    def test_main_divide(self):
        expected = 1
        operands_list = [10, 10]
        actual = main("4", operands_list)
        assert actual == expected

    def test_main_divide_by_zero(self):
        expected = 0
        operands_list = [0, 10]
        actual = main("4", operands_list)
        assert actual == expected


if __name__ == '__main__':
    unittest.main()

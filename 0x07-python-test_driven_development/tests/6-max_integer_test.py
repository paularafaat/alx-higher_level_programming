#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for the max_integer function"""

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_positive_numbers(self):
        """Test for a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test for a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """Test for a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_single_element_list(self):
        """Test for a list with a single element"""
        self.assertEqual(max_integer([100]), 100)

    def test_duplicate_elements(self):
        """Test for a list with duplicate elements"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_float_numbers(self):
        """Test for a list of floating-point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9]), 3.9)

    def test_strings(self):
        """Test for a list of strings"""
        with self.assertRaises(TypeError):
            max_integer(["apple", "banana", "orange"])


if __name__ == "__main__":
    unittest.main()

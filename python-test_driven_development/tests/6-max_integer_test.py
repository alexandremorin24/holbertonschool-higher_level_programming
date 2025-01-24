#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_one_element(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([1, 4, 4, 3]), 4)

    def test_mixed_types(self):
        """Test with integers and floats"""
        self.assertEqual(max_integer([1.5, 2.3, 3.8, 3.1]), 3.8)

    def test_all_negative_floats(self):
        """Test with all negative floats"""
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -0.5]), -0.5)


if __name__ == "__main__":
    unittest.main()

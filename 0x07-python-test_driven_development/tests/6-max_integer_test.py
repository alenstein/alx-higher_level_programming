#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_list_of_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_mixed_values(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'a'])

    def test_list_with_single_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

if __name__ == '__main__':
    unittest.main()


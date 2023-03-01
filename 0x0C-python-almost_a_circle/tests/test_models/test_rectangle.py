#!/usr/bin/python3
""" unittests for the rectangle class attributes and methods"""
import unittest
import sys
sys.path.append("../../models/")

Rectangle = __import__('rectangle').Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_width(self):
        rect = Rectangle(5, 10)
        rect.width = 8
        self.assertEqual(rect.width, 8)
        with self.assertRaises(TypeError):
            rect.width = "eight"
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height(self):
        rect = Rectangle(5, 10)
        rect.height = 12
        self.assertEqual(rect.height, 12)
        with self.assertRaises(TypeError):
            rect.height = "twelve"
        with self.assertRaises(ValueError):
            rect.height = -3

    def test_x(self):
        rect = Rectangle(5, 10)
        rect.x = 3
        self.assertEqual(rect.x, 3)
        with self.assertRaises(TypeError):
            rect.x = "three"
        with self.assertRaises(ValueError):
            rect.x = -2

    def test_y(self):
        rect = Rectangle(5, 10)
        rect.y = 4
        self.assertEqual(rect.y, 4)
        with self.assertRaises(TypeError):
            rect.y = "four"
        with self.assertRaises(ValueError):
            rect.y = -1


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""" unittests for the rectangle class attributes and methods"""

import unittest
Rectangle = __import__('models.rectangle').Rectangle

class TestRectangle(unittest.TestCase):
    def test___init__(self):
        self.assertIsInstance(self, Rectangle)

        
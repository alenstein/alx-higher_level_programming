#!/usr/bin/python3
"""Tests cases for the Base class"""

import unittest
import sys
sys.path.append("../../models/")

from base import Base


class TestBase(unittest.TestCase):
    def test_id_generation(self):
        # Test that ids are generated correctly when no id is passed
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_passing(self):
        # Test that ids are assigned correctly when passed
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_edge_cases(self):
        # Test edge cases for id parameter
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

        b2 = Base(-5)
        self.assertEqual(b2.id, -5)

    def test_private_nb_objects(self):
        # Test that __nb_objects is private
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_instance_attributes(self):
        # Test that instance has correct attributes
        b1 = Base()
        self.assertTrue(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "__nb_objects"))

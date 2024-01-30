#!/usr/bin/python3
"""
This module contains unit testing for the custom base module.
"""
import unittest
from models.base import Base


class CustomBaseTest(unittest.TestCase):
    """ Unit testing for the Base Class
    """
    def test_auto_increment(self):
        custom_base1 = Base()
        custom_base2 = Base()
        self.assertEqual(custom_base2.id, custom_base1.id + 1)

    def test_assigned_id(self):
        custom_base = Base(42)
        self.assertEqual(custom_base.id, 42)

    def test_convert_to_json(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'unique_id': 12}]), "[{\"unique_id\": 12}]")

    def test_convert_from_json(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"unique_id": 34}]'), [{"unique_id": 34}])

if __name__ == "__main__":
    unittest.main()

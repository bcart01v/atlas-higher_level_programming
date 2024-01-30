#!/usr/bin/python3
"""
This module contains unittests for the Rectangle class.
"""
import unittest


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        rect_a = Rectangle(3, 4)
        self.assertIsInstance(rect_a, Rectangle)
        rect_b = Rectangle(3, 4, 5)
        self.assertIsInstance(rect_b, Rectangle)
        rect_c = Rectangle(3, 4, 5, 6)
        self.assertIsInstance(rect_c, Rectangle)

        with self.assertRaises(TypeError):
            Rectangle("3", 4)
        with self.assertRaises(TypeError):
            Rectangle(3, "4")
        with self.assertRaises(ValueError):
            Rectangle(3, 4, -5)
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 5, -6)
        with self.assertRaises(ValueError):
            Rectangle(0, 4)
        with self.assertRaises(ValueError):
            Rectangle(3, 0)

    def test_rectangle_properties(self):
        rect = Rectangle(3, 4, 5, 6)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)

    def test_rectangle_methods(self):
        rect = Rectangle(3, 4, 5, 6)
        self.assertEqual(rect.area(), 12)
        expected_str = f"[Rectangle] ({rect.id}) 5/6 - 3/4"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        rect = Rectangle(3, 4, 5, 6)
        rect.update(77, 3, 4, 5, 6)
        self.assertEqual(rect.id, 77)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)

    def test_to_dictionary(self):
        rect = Rectangle(3, 4, 5, 6)
        dict_repr = rect.to_dictionary()
        expected_dict = {'id': rect.id, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertEqual(dict_repr, expected_dict)

    def test_create(self):
        rect = Rectangle.create(id=7, width=8, height=9, x=10, y=11)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 11)

if __name__ == "__main__":
    unittest.main(exit=False)

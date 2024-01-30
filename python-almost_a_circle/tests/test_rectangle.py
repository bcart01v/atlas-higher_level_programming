#!/usr/bin/python3
"""
This module contains unittests for the Rectangle class.
"""
import unittest
import io
import sys
import os
import json


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

    def test_bad_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-1, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_bad_heigh(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_display_without_xy(self):
        rect = Rectangle(3, 2)
        expected_output = "###\n" * 2

        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display(self):
        rect = Rectangle(4, 3)
        expected_output = "####\n" * 3
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")
        os.remove("Rectangle.json")

    def test_to_file_blank(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")
        os.remove("Rectangle.json")

    def test_to_file_onetwo(self):
        rect = Rectangle(1, 2)
        Rectangle.save_to_file([rect])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            loaded_data = json.loads(contents)
            expected_data = json.loads(json.dumps([rect.to_dictionary()]))
            self.assertEqual(loaded_data, expected_data)
        os.remove("Rectangle.json")

    def test_load_blank(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_existing(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        test_data = [rect1.to_dictionary(), rect2.to_dictionary()]
        with open("Rectangle.json", "w") as file:
            json.dump(test_data, file)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].width, rect1.width)
        self.assertEqual(loaded_rectangles[0].height, rect1.height)
        self.assertEqual(loaded_rectangles[1].width, rect2.width)
        self.assertEqual(loaded_rectangles[1].height, rect2.height)
        os.remove("Rectangle.json")

if __name__ == "__main__":
    unittest.main(exit=False)

#!/usr/bin/python3
"""
This module contains Unit tests for the Square class.
"""
import unittest


from models.square import Square


class TestCustomSquare(unittest.TestCase):

    def test_square_creation(self):
        square_one = Square(5)
        square_two = Square(5, 10)
        square_three = Square(5, 10, 15)

        self.assertIsInstance(square_one, Square)
        self.assertIsInstance(square_two, Square)
        self.assertIsInstance(square_three, Square)

        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(TypeError):
            Square(5, "10")
        with self.assertRaises(TypeError):
            Square(5, 10, "15")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -10)
        with self.assertRaises(ValueError):
            Square(5, 10, -15)
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_properties(self):
        square = Square(10, 20, 30, 40)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)

    def test_str(self):
        square = Square(10, 20, 30, 40)
        self.assertEqual(str(square), "[Square] (40) 20/30 - 10")

    def test_to_dictionary(self):
        square = Square(10, 20, 30, 40)
        dict_repr = square.to_dictionary()
        self.assertEqual(dict_repr, {'id': 40, 'size': 10, 'x': 20, 'y': 30})

    def test_update(self):
        square = Square(10, 20, 30, 40)
        square.update(88, 10, 20, 30)
        self.assertEqual(square.id, 88)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)

    def test_create(self):
        square = Square.create(id=6, size=12, x=18, y=24)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 12)
        self.assertEqual(square.x, 18)
        self.assertEqual(square.y, 24)


if __name__ == "__main__":
    unittest.main()

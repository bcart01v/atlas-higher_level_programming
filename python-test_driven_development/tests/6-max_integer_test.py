"This is an actual unit test for max_integer([..])"


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function."""

    def test_max(self):
        "Empty List"
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        "Single element"
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-20]), -20)
        self.assertEqual(max_integer([500]), 500)

    def test_negative_numbers(self):
        "Negative numbers"
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, -2, -3, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -3, -500]), -1)

    def test_mixed_numbers(self):
        "Mixed numbers"
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([1, 2, -3, 0]), 2)
        self.assertEqual(max_integer([1, 2, -3, 500]), 500)

    def test_mixed_types(self):
        "Mixed types"
        self.assertEqual(max_integer([1, 2.9, 3.1]), 3.1)
        self.assertEqual(max_integer([1, 2, 5.5, 0]), 5.5)
        self.assertEqual(max_integer([1.3, 2, 3, -500]), 3)

    def test_type_error(self):
        "Test that a TypeError is actually happpening for invalid input"
        with self.assertRaises(TypeError):
            max_integer(1, "Pofart", 5)
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()

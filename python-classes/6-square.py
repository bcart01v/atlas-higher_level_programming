#!/usr/bin/python3
"""Module Docstring: This module provides a Square class with size and position attributes."""


class Square:
    """Class to represent a square with size and position.

    Attributes:
        size (int): The size of the square's side. Must be a non-negative integer.
        position (tuple): The (x, y) position of the square. Both x and y must be non-negative integers.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square using the '#' character, offset by its position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            position (tuple, optional): The (x, y) position of the square. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: The size of the square's side with a property getter and setter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square's side.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The (x, y) position of the square with a property getter and setter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the (x, y) position of the square.

        Args:
            value (tuple): The new (x, y) position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or 
            len(value) != 2 or 
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character, offset by its position."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

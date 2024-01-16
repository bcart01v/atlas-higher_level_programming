#!/usr/bin/python3
"""Module Docstring: This module provides a
Square class used to represent a square."""


class Square:
    """Class to represent a square.

    Attributes:
        size (int): The size of the square's side.
        Must be a non-negative integer.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square using the '#' character.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """int: The size of the square's side with
        a property getter and setter."""
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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

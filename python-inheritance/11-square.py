#!/usr/bin/python3

""" Module: 10-square.py
    This module contains the Square class

    Classes:
        Square - inherits from Rectangle

    Functions:
        None

    Usage:
        Not for external use
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class: Square
        Inherits from Rectangle

        Methods:
            None
    """
    def __init__(self, size):
        """ __init__
            __ = Private.
            Initializes the Square class.

            Attributes:
                size (int): the size of the square.

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area
            Calculates the area of the Square.

            Attributes:
                None

        """
        return self.__size * self.__size

    def __str__(self):
        """ __str__
            Returns a string representation of the Square.

            Attributes:
                None

        """
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3

"Module 8-rectangle.py. this module contains the Rectangle Class."

BaseGeometry = __import__('7-base_geometry').BaseGeometry


""" Module: 8-rectangle.py
    This module contains the Rectangle class

    Classes:
        Rectangle - inherits from BaseGeometry
        BaseGeometry - A class that validates value mostly.

    Functions:
        None

    Usage:
        Not for now.
"""

class Rectangle(BaseGeometry):
    """ Class: Rectangle
        Inherits from BaseGeometry

        Methods:
            None
    """
    def __init__(self, width, height):
        """ __init__
            __ = Private.
            Initializes the Rectangle class.

            Attributes:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area
            Calculates the area of the Rectangle.

            Attributes:
                None

        """
        return self.__width * self.__height

    def __str__(self):
        """ __str__
            Returns a string representation of the Rectangle.

            Attributes:
                None

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

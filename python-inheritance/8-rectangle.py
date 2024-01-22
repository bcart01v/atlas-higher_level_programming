#!/usr/bin/python3

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

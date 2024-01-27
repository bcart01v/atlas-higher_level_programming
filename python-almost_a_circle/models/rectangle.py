#!/usr/bin/python3
""" 
This module, in it's current state, provides the Rectangle class
which inherits from the Base class. It's presumed to represent
rectangular shapes with various properties.
"""

from models.base import Base

class Rectangle(Base):
    """ A Rectangle class to represent... well, a Rectangle.

    Attributes: 
    width (int): Width of the Rectangle
    height (int): Height of the Rectangle
    x (int): x - Coordinate of Rectangle
    y (int): y - Coordinate of Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init Function

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
            x (int): Coordinate of the Rectangle. Defaults to 0.
            y (int): Coordinate of the Rectangle. Defaults to 0.
            id (_type_): The ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


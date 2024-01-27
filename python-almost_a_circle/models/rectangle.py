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
        
        self._ValidateCheck(width, 'width', 0)
        self._ValidateCheck(height, 'height', 0)
        self._ValidateCheck(x, 'x')
        self._ValidateCheck(y, 'y')
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def _ValidateCheck(self, value, name, min_value = 0):
        """ Instead of doing the same check 100 times,
        I wanted a way to check in one spot. This is that
        one spot.

        Args:
        value(int): The value we are validating
        name(str): The name it's validating
        min_value (int): The minimum we can accept. Default of 0

        Raises:
            TypeError if value is not an Integer
            ValueError if the value is < 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"]:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"]:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self._ValidateCheck(value, 'width', 0)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self._ValidateCheck(value, 'height', 0)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self._ValidateCheck(value, 'x', 0)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self._ValidateCheck(value, 'y', 0)
        self.__y = value

#!/usr/bin/python3
"""Module 7-rectangle"""


class Rectangle:
    """Rectangle class with width and height"""
    number_of_instances = 0
    default_print_symbol = "#"
    debug = 0

    def __init__(self, width=0, height=0):
        """Initialization with optional width and height"""
        self.width = width
        self.height = height
        self._instance_symbol = None
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        if self.__width == 0 or self.__height == 0:
            print()
            return
        for i in range(self.__height):
            print(self.print_symbol * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        print_symbol = str(self.print_symbol)
        return "\n".join([print_symbol * self.__width] * self.__height)

    def __repr__(self):
        """Eval string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def print_symbol(self):
        """Print symbol"""
        if Rectangle.debug == 1:
            Line1 = "Debug: print_symbol value is"
            Line2 = self._instance_symbol or Rectangle.print_symbol
            Line3 = Rectangle.print_symbol
            print(Line1, Line2 or Line3)

        if self._instance_symbol is not None:
            return self._instance_symbol
        return Rectangle.default_print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        self._instance_symbol = value

    def __del__(self):
        """Delete Object, we're done."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

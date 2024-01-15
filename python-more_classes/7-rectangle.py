#!/usr/bin/python3
"""Module 7-rectangle"""


class Rectangle:
    """Rectangle class with width and height"""
    number_of_instances = 0

    def __init__(self, width=0, height=0, print_symbol="#"):
        """Initialization with optional width and height"""
        self.width = width
        self.height = height
        self.print_symbol = print_symbol
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
        """Print rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
            return
        symbol = str(self.print_symbol)
        for i in range(self.__height):
            print(symbol * self.__width)

    def __str__(self):
        """String representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self):
        """Eval string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)



    def __del__(self):
        """Delete Object, we're done."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

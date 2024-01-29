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

    def area(self):
        """
        The function calculates the area of a the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """ This function prints a visual representation of
        the rectangle
        """
        for eachline in range(self.__y):
            print()
        for eachrow in range(self.__height):
            for eachspace in range(self.__x):
                print(" ", end="")
            for eachchar in range(self.__width):
                print ("#", end="")
            print()

    def __str__(self):
        """ This function returns the a custom version of
        what str would return.

        Returns:
            [Rectangle] (id) x/y width/height
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, \
            self.__width, self.__height)

    def update(self, *args):
        """
        The update function takes in any number of arguments and does something with them.
        """
        if len(args) > 0:
            self.__id  = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__x = args[4]


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

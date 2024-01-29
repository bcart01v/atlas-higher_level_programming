#!/usr/bin/python3

""" Square! This model inherits from Rectangle, which makes since,
    Because a square is a rectangle with the same dimension.
    """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ A Square class, similar to Rectangle. Which will be
    a visual representation of a square.

    Attributes:
        size(int): Size of the square
        x(int): Coordinate of the square
        y(int): coordinate of the square
    """
    def __init__ (self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Custom STR function.
        Needs to say Square, not Rectangle.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,\
            self.y, self.width)

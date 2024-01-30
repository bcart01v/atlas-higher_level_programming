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
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Custom STR function.
        Needs to say Square, not Rectangle.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """We update the square. Default to args,
        If args is empty, we use kwargs.
        """
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ Dictionary for Square """
        sqa_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return sqa_dict

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        self._ValidateCheck(value, 'width', 0)
        self.width = value
        self.height = value

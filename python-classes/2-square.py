#!/usr/bin/python3

"Another Square Class"


class Square:
    """This is a class that defines a square"""
    def __init__(self, size=0):
        """This is a function that defines the size of the square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

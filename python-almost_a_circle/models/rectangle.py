#!/usr/bin/python3

""" Rectangle class """
from models.base import Base

def __init__(self, width, height, x=0, y=0, id=None):
    """ Constructor """
    super().__init__(id)
    self.__width = width
    self.__height = height
    self.__x = x
    self.__y = y

@property
def width(self):
    """ Getter """
    return self.__width

@width.setter
def width(self, value):
    """ Setter """
    # This will probably need validation of some sort.
    self.__width = value

@property
def height(self):
    """ Getter """
    return self.__height

@height.setter
def height(self, value):
    """ Setter """
    # This will probably need validation of some sort
    self.__height = value

@property
def x(self):
    """ Getter """
    return self.x

@x.setter
def x(self, value):
    """ Setter """
    self.x = value

@property
def y(self):
    """getter"""
    return self.y

@y.setter
def y(self, value):
    """ Setter """
    self.y = value
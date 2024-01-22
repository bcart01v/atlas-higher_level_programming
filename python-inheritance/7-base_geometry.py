#!/usr/bin/python3

""" Module: 7-base_geometry.py
    
        This module contains the BaseGeometry class
    
        Functions:
            def area(self) - Raises an exception.
            def integer_validator(self, name, value) - Validates value.
    
        Attributes:
            Only raises an exception (for now)
    """


class BaseGeometry:
    """ BaseGeometry class
    
    The BaseGeometry class provides a method for calculating the area
    of a shape and a method for validating integers.
    
    """
    def area(self):
        """
        This currently only raises an exception.
        
        Args:
        self: the object itself.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator

        Args:
            self: the object itself.
            name (str): the name of the variable.
            value (int): the value of the variable.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

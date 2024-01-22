#!/usr/bin/python3

""" Module: 6-base_geometry.py

    This module contains the BaseGeometry class

    Classes:
        BaseGeometry - It's an empty class.

    Functions:
        def area(self) - Raises an exception.

    Usage:
        Only raises an exception (for now)
"""


class BaseGeometry:
    """ BaseGeometry class

        No longer an empty class, we have area now.
        Except the area only returns an exception.


    """
    def area(self):
        """ area function

        It's a public instance method.

    """
        raise Exception("area() is not implemented")

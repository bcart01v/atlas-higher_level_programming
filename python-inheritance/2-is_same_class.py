#!/usr/bin/python3

""" Module: 2-is_same_class.py
"""

class IsSameClass:
    """Class to check if an object is the same as the specified class
    
    Functions:
        is_same_class(obj, a_class) - Returns True if the object is exactly an
        instance of the specified class; otherwise False.
    
    Usage:
        Used to check if an object is the same as the specified class
    """ 

    def is_same_class(obj, a_class):
        """ Checks if an object is the same as the specified class
        """
        return type(obj) is a_class

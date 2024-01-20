#!/usr/bin/python3

""" Module: 2-is_same_class.py
"""

class is_same_class:
    """Class to check if an object is the same as the specified class
    
    Function:
    is_same_class(obj, a_class) - Returns True if the object is exactly an
        instance of the specified class; otherwise False.
    
    Usage:
        Used to check if an object is the same as the specified class
    """ 

    def is_kind_of_same_class(obj, a_class):
        """
        Check if object is an instance of the specified class
        
        Args:
            obj - The object to check
            a_class - The class to check against
        
        Returns:
            True if the object is exactly an instance of the specified class;
            otherwise False.
        """
        return type(obj) == a_class

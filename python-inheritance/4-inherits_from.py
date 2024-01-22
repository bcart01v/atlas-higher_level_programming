#!/usr/bin/python3

""" Module: 4-inherits_from.py
    This module contains the inherits_from function

    Functions:
        inherits_from(obj, a_class) - Checks if an object is an instance of a
        class that inherited (directly or indirectly) from the specified class.

    Usage:
        Used to check if an object is an instance of a class that inherited
        (directly or indirectly) from the specified class.

"""


def inherits_from(obj, a_class):
    """ Function: inherits_from
        Checks if an object is an instance of a class that inherited
        from the specified class.

        Args:
            obj (object): The object to check
            a_class (class): The class to check against

        Returns:
            True if obj is an instance of a class that inherited (directly or
            indirectly) from the specified class; otherwise False.

    """
    return isinstance(obj, a_class) and type(obj) != a_class

#!/usr/bin/python3

""" 
Module: 0-lookup.py

Functions:
    lookup(obj) - Returns a list containing the names of all the attributes and
    methods of the specified object.

Usage:
    Used to return a list of attributes and methods of an object

"""

def lookup(obj):
    """ Returns the list of available attributes and methods of an object
    """
    return dir(obj)

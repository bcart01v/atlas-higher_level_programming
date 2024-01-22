#!/usr/bin/python3

"""Class to JSON module. Returns the dictionary description with simple data"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__

#!/usr/bin/python3


""" Base class """
import json

class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A JSON implimentation"""
        if (list_dictionaries) is None or \
            not list_dictionaries:
                return "[]"
        else:
            return json.dumps(list_dictionaries)
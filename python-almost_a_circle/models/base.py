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

    @classmethod
    def save_to_file(cls, list_objs):
        """ A method that builds a json file based on
        parameters passed to the method. """
        dict_list = []
        if list_objs:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        json_string = cls.to_json_string(dict_list)

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            file.write(json_string)

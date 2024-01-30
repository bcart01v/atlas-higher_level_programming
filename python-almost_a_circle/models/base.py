#!/usr/bin/python3


""" Base class """
import json
import os

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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or \
            len(json_string) == 0:
                return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create a dummy instance of a class,
        then apply the dictionary values to said instance """
        if cls.__name__ == 'Square':
            temp_instance = cls(1, 0, 0)
        else:
            temp_instance = cls(1, 1, 0, 0)

        temp_instance.update(**dictionary)
        return temp_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

        list_dicts = cls.from_json_string(json_string)

        instances = [cls.create(**dct) for dct in list_dicts]

        return instances

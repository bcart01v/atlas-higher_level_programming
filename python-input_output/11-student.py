#!/usr/bin/python3

"""Module for Student Class"""


class Student:
    """Student class. For each student, his/her first name, last name and age
    will be saved"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function. Also checks if the types are correct and
        if the age is a positive number"""
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
        if type(age) is not int:
            raise TypeError("age must be an integer")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            self.__dict__[key] = json[key]

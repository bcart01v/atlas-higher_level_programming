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
        if age < 0:
            raise TypeError("age must be >= 0")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description with simple data structure"""
        return self.__dict__
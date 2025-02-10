#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.
        """
        for key, value in json.items():
            setattr(self, key, value)

#!/usr/bin/python3
"""
Module that provides a function to convert a class instance to a dictionary
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object's attributes
    for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all serializable attributes
        of the object.
    """
    return (obj.__dict__)

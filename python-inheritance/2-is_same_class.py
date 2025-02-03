#!/usr/bin/python3
"""
Returns True if the object is exactly
an instance of the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of a specified class.
    """
    return type(obj) is a_class

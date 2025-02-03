#!/usr/bin/python3
"""
This module defines the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class or a subclass.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

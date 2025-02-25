#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class used to represent BaseGeometry.
    """

    def area(self):
        raise Exception("area() is not implemented")

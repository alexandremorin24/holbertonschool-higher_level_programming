#!/usr/bin/python3
"""
Defines BaseGeometry class with area and integer validation methods.
"""


class BaseGeometry:
    """
    A class used to represent BaseGeometry.
    """

    def area(self):
        """Raises an exception as area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

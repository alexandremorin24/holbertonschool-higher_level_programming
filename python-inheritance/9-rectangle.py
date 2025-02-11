#!/usr/bin/python3
"""
Defines BaseGeometry and Rectangle classes.
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


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """Returns the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"

#!/usr/bin/python3
"""
Defines an empty class Rectangle.
"""


class Rectangle:
    """
    Represents a Rectangle with validated width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.
        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Validates that width is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Validates that height is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

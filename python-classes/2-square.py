#!/usr/bin/python3
"""
Module 2-square
Defines a class Square with validation for the size attribute.
"""


class Square:
    """
    Represents a square.
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a validated size.
        Args:
            size (int): The size of the square, must be >= 0.
        Raises:
            ValueError: If size is not an integer or is less than 0.
        """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

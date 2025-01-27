#!/usr/bin/python3
"""
Module 4-square
Defines a class Square with a private attribute size,
a getter and setter for size, and a method to compute the area.
"""


class Square:
    """
    Represents a square.
    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.
        Args:
            size (int): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.
        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for the size attribute.
        Validates the size value before setting it.
        Args:
            size (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

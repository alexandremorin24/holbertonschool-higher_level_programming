#!/usr/bin/python3
"""
Module 6-square
Defines a class Square with private attributes size and position,
with methods to compute the area and print the square.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a validated size.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute.
        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        Validates that size is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.
        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.
        Validates that position is a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(coord, int) and coord >= 0 for coord in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character #, considering the position.
        If size is 0, prints an empty line.
        """
        print("\n" * self.__position[1], end="")

        if self.__size == 0:
            print()
        else:
            for line in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

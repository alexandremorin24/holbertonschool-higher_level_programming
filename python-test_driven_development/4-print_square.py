#!/usr/bin/python3
"""
This module provides a function `print_square` that prints
a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character `#`.

    The square has a side length equal to `size`.

    Args:
        size (int): The size of the square's side. Must be a positive integer.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square("Two")
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer

        >>> print_square(-2)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0

        >>> print_square(2.15)
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

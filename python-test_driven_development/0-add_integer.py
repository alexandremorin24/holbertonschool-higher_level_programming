#!/usr/bin/python3
"""
This module provides a function `add_integer` for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casts them to integers if needed).

    Args:
        a (int, float): The first number.
        b (int, float): The second number, default is 98.

    Returns:
        int: The addition of `a` and `b`.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        Traceback (most recent call last):
        ...
        TypeError: b must be an integer
        >>> add_integer(None)
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b(int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

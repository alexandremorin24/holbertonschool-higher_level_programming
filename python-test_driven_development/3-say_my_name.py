#!/usr/bin/python3
"""
This module provides a function `say_my_name` that prints:
"My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".
    Strips leading and trailing spaces from both `first_name` and `last_name`.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print. Defaults to an empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Heisenberg")
        My name is Heisenberg
        >>> say_my_name(None, "Smith")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string
        >>> say_my_name("John", None)
        Traceback (most recent call last):
            ...
        TypeError: last_name must be a string
        >>> say_my_name("   John   ", "   ")
        My name is John
        >>> say_my_name("   ", "   ")
        My name is
    """

    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name.strip(), last_name.strip()))

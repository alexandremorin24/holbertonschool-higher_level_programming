#!/usr/bin/python3
"""
This module provides a function `text_indentation` that prints
a text with 2 new lines after each of
these characters: . , ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, and :.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If `text` is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I am fine: thanks.")
        Hello.

        How are you?

        I am fine:

        thanks.
    """

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    separator = ".?:"

    for sep in ".?:":
        text = text.replace(sep, sep + "\n\n")

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    formatted_text = "\n".join(lines)

    print(formatted_text)

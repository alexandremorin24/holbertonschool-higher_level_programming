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
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Build the result with two new lines after each separator
    result = ""
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            # Add two new lines after a separator
            result += "\n\n"
            i += 1
            # Skip spaces after separator
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        result += text[i]
        i += 1

    # Print the result, ensuring no leading/trailing spaces on each line
    print("\n\n".join(line.strip()
          for line in result.split("\n") if line.strip()))

#!/usr/bin/python3
"""
Module for serializing and deserializing a dictionary with XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def convert_type(value):
    """
    Converts a string to int, float, or keeps it as str.

    Args:
        value (str): The value to convert.

    Returns:
        int | float | str: The converted value.
    """
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value


def deserialize_from_xml(filename):
    """
    Reads an XML file and converts it back to a dictionary.

    Args:
        filename (str): The input XML filename.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for element in root:
        data[element.tag] = convert_type(element.text)

    return data

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
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            element = ET.SubElement(root, key)
            element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception as e:
        print(f"Error during serialization: {e}")


def convert_type(value):
    """
    Converts a string to int, float, bool, or keeps it as str.

    Args:
        value (str): The value to convert.

    Returns:
        int | float | bool | str: The converted value.
    """
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    elif value.isdigit():
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
        dict | None: The deserialized dictionary or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for element in root:
            data[element.tag] = convert_type(element.text)

        return data

    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error during deserialization: {e}")
        return None

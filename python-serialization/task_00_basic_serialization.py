#!/usr/bin/python3
"""
Module for basic JSON serialization and deserialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Saves a dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """Loads a dictionary from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

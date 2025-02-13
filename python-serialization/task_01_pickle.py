#!/usr/bin/python3
"""
Module defining the CustomObject class with serialization and deserialization.
"""

import pickle


class CustomObject:
    """Represents a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            print("Error during serialization")

    @classmethod
    def deserialize(cls, filename):
        """Loads an instance of CustomObject from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print("Error during deserialization")
            return None

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

    def display(self):
        """Displays the attributes of the object in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return True  # ✅ Ajout du return True
        except Exception as e:
            print(f"Error during serialization: {e}")
            return False  # ✅ Retourne False en cas d'échec

    @classmethod
    def deserialize(cls, filename):
        """Loads an instance of CustomObject from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error during deserialization: {e}")
            return None  # ✅ Gère les fichiers vides

#!/usr/bin/python3
"""
Defines an abstract class Animal and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    It enforces the implementation of the `sound` method in subclasses.
    """
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Class representing a Dog, inheriting from Animal."""

    def sound(self):

        return "Bark"


class Cat(Animal):
    """Class representing a Cat, inheriting from Animal."""

    def sound(self):
        return "Meow"

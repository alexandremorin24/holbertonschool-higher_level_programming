#!/usr/bin/python3
"""
Defines Fish, Bird, and FlyingFish classes demonstrating multiple inheritance.
"""


class Fish:
    """
    Represents a fish with the ability to swim and a specific habitat.
    """

    def swim(self):
        """Prints a message indicating that the fish is swimming."""
        print("The fish is swimming.")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water.")


class Bird:
    """
    Represents a bird with the ability to fly and a specific habitat.
    """

    def fly(self):
        """Prints a message indicating that the bird is flying."""
        print("The bird is flying.")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that can both swim and fly.
    """

    def fly(self):
        """Prints a message indicating that the flying fish is flying."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")

#!/usr/bin/python3
"""
Defines mixins for swimming and flying abilities, and a Dragon class using them.
"""


class SwimMixin:
    """
    Mixin providing swimming capability.
    """

    def swim(self):
        """Prints a message indicating that the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin providing flying capability.
    """

    def fly(self):
        """Prints a message indicating that the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that can both swim and fly.
    """

    def roar(self):
        """Prints a message indicating that the dragon can roar."""
        print("The dragon roars!")

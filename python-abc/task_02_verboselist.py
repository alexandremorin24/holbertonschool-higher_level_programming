#!/usr/bin/python3
"""
Defines a custom list class VerboseList that extends list.
It prints notifications when elements are added or removed.
"""


class VerboseList(list):
    """
    Custom list class that prints messages when modifying the list.
    """

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, items):
        """Extends the list with multiple items and prints a notification."""
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        Checks if the item exists before trying to remove it.
        """
        if item in self:
            print(f"Removed {item} from the list")
            super().remove(item)
        else:
            print(f"Error: {item} not found in the list.")

    def pop(self, index=None):
        """
        Removes and returns an item from the list.
        Prints a notification for the removed item.
        """
        if index is None:
            item = super().pop()
            print(f"Popped {item} from the list.")
        else:
            item = super().pop(index)
            print(f"Popped {item} from the list at index {index}.")
        return item

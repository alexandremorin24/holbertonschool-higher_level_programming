#!/usr/bin/python3
"""
Defines CountedIterator, an iterator that counts the number of items iterated.
"""


class CountedIterator:
    """
    Custom iterator that tracks the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and iteration counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Returns the iterator itself.
        """
        return self

    def __next__(self):
        """
        Fetches the next item from the iterator while counting iterations.
        Raises StopIteration when the iterator is exhausted.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Returns the number of items that have been iterated over.
        """
        return self.count

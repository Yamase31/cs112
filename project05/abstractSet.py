"""
Author: Harry Pinkerton, James Lawson, Laurie Jones
File: abastractSet.py
Project: 5
"""

from abstractCollection import AbstractCollection

class AbstractSet(AbstractCollection):
    """stuff goes here"""

# Mutator Methods

    def __or__(self, other):
        return self + other

    def __and__(self, other):
        newList = []

        for i in self:
            if i in other:
                newList.append(i)
        return newList

    def __sub__(self, other):
        for item in self:
            if item not in other:
                return item

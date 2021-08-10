"""
Author: Harry Pinkerton, James Lawson, Laurie Jones
File: arraySortedSet.py
Project: 5
"""

from abstractCollection import AbstractCollection
from abstractSet import AbstractSet
from arrays import Array
from abstractBag import AbstractBag
from arraySortedBag import ArraySortedBag
from arraySet import ArraySet

class ArraySortedSet(ArraySet, ArraySortedBag ):
    """An array-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        super().__init__(sourceCollection)

    # Mutator Methods
    def __eq__(self, other):
        if self is other: return True

        if type(self) != type(other): return False

        if len(self) != len(other): return False

        for item in self:
            if item not in other:
                return False
            
        for item in other:            
            if not item in self:                
                return False 

        return True

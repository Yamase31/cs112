"""
Author: Harry Pinkerton, James Lawson, Laurie Jones
File: arraySet.py
Project: 5
"""
from arrayBag import ArrayBag
from abstractCollection import AbstractCollection
from node import Node
from abstractSet import AbstractSet


class ArraySet(AbstractSet, ArrayBag):
    """stuff goes here"""

    #Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        self._items = None
        super().__init__(sourceCollection)

    # Accessor Methods
    def __eq__(self,other):
        AbstractCollection.__eq__(self, other)

        
    # Mutator Methods
    def add (self,item):
        if item not in self:
         #ArrayBag
             super().add(item)

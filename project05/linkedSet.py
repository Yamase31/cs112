"""
Author: Harry Pinkerton, James Lawson, Laurie Jones
File: linkedSet.py
Project: 5
"""
from linkedBag import LinkedBag
from abstractCollection import AbstractCollection
from abstractSet import AbstractSet
from node import Node


class LinkedSet(AbstractSet, LinkedBag):
    """stuff goes here"""

    #Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        self._items = None
        super().__init__(sourceCollection)


     # Accessor Methods
##    def __eq__(self,other):
##        AbstractCollection.__eq__(self, other)
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




    # Mutator Methods

    def add (self, item):
        if item not in self:
         #LinkedBag
             super().add(item)




    

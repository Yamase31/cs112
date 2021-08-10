"""
File: linkedBag.py
Project: 4
Author: James Lawson, Harrison Pinkerton, Laruie Jones
Creates a linked bag
"""
from node import Node
from abstractBag import AbstractBag


class LinkedBag(AbstractBag):
    """A link-based implemention of a bag."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        self._items = None
        super().__init__(sourceCollection)

    # Accessor Methods

    def __iter__(self):
        before = super().getModCount()
        cursor = self._items

        while cursor != None:
            yield cursor.data
            after = super().getModCount()
            
            if before == after:
                cursor = cursor.next
            else:
                raise AttributeError("Illegal modification of the backing store.")
        
    # Mutator Methods
    def clear(self):
        self._size = 0
        self._items = None
        super().resetSizeAndModCount()

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1
        super().incModCount()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        cursor = self._items
        trailer = None

        if item not in self:
            raise IndexError("item is removed from self")
        
        for i in self:
            if item == i:
                break
            trailer = cursor
            cursor = cursor.next

        if cursor == self._items:
            self._items = None
            
        else:
            trailer.next = cursor
        
            
        self._size -= 1
        super().incModCount()
        

if __name__ == "__main__":
    a = LinkedBag(["hi", "bye", "cat"])
    b = LinkedBag(["a", "b", "c"])

    print(a + b)

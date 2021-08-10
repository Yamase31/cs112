"""
File: arrayQueue.py
Author: Laurie Jones

Make sure to have your array resize itself, both growing and shrinking, at the appropriate locations.
"""

from .arrays import Array
from .abstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = -1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)


    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        #  to wrap the cursor around the end of the array
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[(cursor + self._front)%len(self._items)]
            if myModCount != self._modCount:
                raise AttributeError("Cannot modify!")
            cursor += 1

    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
            
        if self.isEmpty():
            raise AttributeError("Queue is empty")
        return self._front    


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._front = self._rear = None
        
    
    def grow(self):
        tempArray = Array(len(self._items) * 2)
        index = 0
        for i in self:
            tempArray[index] = i
            index += 1
        self._rear = len(self)-1
        self._front = 0
        self._items = tempArray
        


    def shrink(self):
        if len(self) // 2 > ArrayQueue.DEFAULT_CAPACITY:
            pass
        
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if len(self) == len(self._items):
            self.grow()
            
        if self.isEmpty() :
            self._front = self._rear = 0
        else:
            self._rear += 1
            self._rear %= len(self._items)
              
        self._items[self._rear] = item
        self._size += 1
        self._modCount += 1



    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        data = self._items[self._front]
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear = -1
        else:
            self._front += 1
            self._front %= len(self._items)
        return data

        


        
         

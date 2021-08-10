"""
File: arraySortedBag.py
Author: James Lawson, Harrison Pinkerton, Laruie Jones
A tester program for bag implementations.
"""

from arrays import Array
from abstractBag import AbstractBag

class ArraySortedBag(AbstractBag):
    """An array-based bag implementation."""


    # Class variables
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    def __contains__ (self):
        """ implements a more efficient search algorithm"""
        #write this
        

    # Accessor Methods
    def __iter__(self):
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[cursor]
            if myModCount != self._modCount:
                raise AttributeError("Cannot modify!")
            cursor += 1            

    # Mutator Methods
    def clear(self):
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        self._modCount += 1

    def add(self, item):
        # resize here if needed
        if len(self._items) == len(self):
            self.grow()
        
        self._items[len(self)] = item
        self._size += 1
        self._modCount += 1

        for i in self:
            if i == len(self._items):
                i += 1
            if item < self._items[i]:
                self._items[index] = newItem
            if item > self._items[i]:
                return
            
            
            
            if self._items[j] > self._items[j -1]:
                self._items[index] = newItem
        self._size += 1
        index += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        tIndex = 0
        for i in range(len(self._items)):
            if item == self._items[i]:
                tIndex = i
                break
            if i == len(self):
                raise IndexError("item is removed from self")
            
        for j in range(tIndex, len(self)-1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        if self._size < .25*len(self._items):
            self.shrink()

    def grow(self):
        """Doubles in size"""
        tempArray = Array(len(self) * 2)
        for i in range(len(self)):
            tempArray[i] = self._items[i]
        self._items = tempArray
        pass

    def shrink(self):
        """Becomes half the current size, does not become smaller than
             initial capacity."""
        half = int(len(self._items) / 2)
        halfArray = Array(half)
        if half > ArrayBag.DEFAULT_CAPACITY:
            for i in range(len(self)):
                halfArray[i] = self._items[i]
            self._items = halfArray
        else:
            pass
                

if __name__ == "__main__":
    a = ArraySortedBag()
    b = ArraySortedBag(["a", "b", "c"])

    a.add("hi")
    a.add("bye")
    a.add("cat")

    print(a)
    print(type(a + b))

    a2 = ArraySortedBag(a)
    print(a2)

    for item in a:
        print(item)

    a.clear()
    print(a)


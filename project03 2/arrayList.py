"""
Names: James Lawson, Harry Pinkerton, Laurie Jones

File: arrayList.py
Project: 3
"""


from arrays import Array

import random

class ArrayList(object):
    """Simulates a List object using an Array"""
    
    def __init__(self, capacity = 10, fillValue = None):
        """Creates an internal Array to store items of the capacity.
             Should also create any other instance variables here."""
        self._defaultFill = fillValue
        self._items = Array(capacity, fillValue)
        self._logicalSize = 0
        self._initialCapacity = 10

    def __len__(self):
        """Returns the capacity of the ArrayList"""
        return len(self._items)

    def __str__(self):
        """Returns a string representation of the ArrayList of the format
           [a, b, c, ... , z]
           Does not show any empty items."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __iter__(self):
        """Returns default iterator. Must set up an instance variable
             to keep track of the current iteration place."""
        cursor = 0
        while cursor < self._logicalSize:
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, index):
        if 0 <= index and index < self.size():
            return self._items[index]

        else:
            raise IndexError(\
                "The index is out of range")

    def __setitem__(self, index, newItem):
        if 0 <= index and index < self.size():
            self._items[index] = newItem
            return self._items[index]
        
        else:
            raise IndexError(\
                "The index is out of range")
        
    def __eq__(self, other):
        """Returns true if the other is an ArrayList and has the same
             contents as self."""
        if self is other: return True

        if type(self) != type(other): return False

        if self.size() != other.size(): return False

        for index in range(self.size()):
            if self._items[index] != other._items[index]:
                return False
        return True

    def size(self):
        """Returns the number of actual items in the array."""
        return self._logicalSize

    def grow(self):
        """Doubles in size"""
        tempArray = Array(len(self) * 2, self._defaultFill)
        for i in range(len(self)):
            tempArray[i] = self._items[i]
        self._items = tempArray
        pass

    def shrink(self):
        """Becomes half the current size, does not become smaller than
             initial capacity."""
        half = int(len(self._items) / 2)
        halfArray = Array(half, self._defaultFill)
        if half > self._initialCapacity:
            for i in range(self._logicalSize):
                halfArray[i] = self._items[i]
            self._items = halfArray
        else:
            pass

    def insert(self, index, newItem):
        """Inserts a new item at the provided index. Resizes if the
             number of items in the ArrayList equals its current
             capacity."""

        if len(self._items) == self._logicalSize:
            self.grow()

        for j in range(index, 1, 1):
            self._items[j] = self._items[j -1]
        self._items[index] = newItem
        self._logicalSize += 1
        index += 1
            
        pass

    def pop(self, index):
        """Pops the item at the provided index. Resizes if the number
             of items in the ArrayList equals one fourth its current
             capacity."""
        for j in range(index, self._logicalSize - 1):
            self._items[j] = self._items[j + 1]
        self._logicalSize -= 1
        if self._logicalSize < .25*len(self._items):
            self.shrink()
            
        pass

    def append(self, newItem):
        """Appends an item to the end of the array. Resizes if the number
             of items in the ArrayList equals its current capacity."""
        self._logicalSize += 1

        if numCount < len(self._items):
            self._items[numCount] = data
            numCount += 1
        pass


def testArrayList():
    """Tests the functionality of the ArrayList class"""

    AL1 = ArrayList()
    AL2 = ArrayList(25)


    print("Capacity of AL1:", len(AL1))
    print("Size of AL1:", AL1.size())

    print("Capacity of AL2:", len(AL2))
    print("Size of AL2:", AL2.size())


    print("\nPutting 30 random numbers into AL1")

    for i in range(30):
        AL1.insert(i, random.randint(1,10))
       

    print("\nCapacity of AL1:", len(AL1))
    print("Size of AL1:", AL1.size())

    print("AL1 equal to AL2:", AL1 == AL2)

    print("\nCopying contents into AL2")
    for i in range(30):
        AL2.insert(i, AL1[i])
       

    print("\nAL1 equal to AL2:", AL1 == AL2)

    print(AL1)
    print(AL2)

    print("\nIterator test:")

    for i in AL1:
        print(i, end=" ")

    print("\n\nRemoving 30 items randomly from AL1")
    for i in range(29,-1,-1):
        AL1.pop(i)
       

    print(AL1)

    


if __name__ == "__main__":
    testArrayList()
    

    

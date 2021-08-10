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
        cursor = self._items

        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def count(self, item):
        ''' this notes each time that a certain value is in a linked structre '''
        count = 0

        for i in self:
            if i == item:
                count += 1
        return count
        

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if other is self:
            return True
        if len(other) != len(self):
            return False
        if len(other) != len(self):
            return False
        if type(other) != type(self):
            return False
        for item in other:
            if self.count(item) != other.count(item):
                return False
            else:
                return True

    

    # Mutator Methods
    def clear(self):
        self._size = 0
        self._items = None

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        cursor = self._items
        trailer = None
        
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
    a = LinkedBag(["hi", "bye", "cat"])
    b = LinkedBag(["a", "b", "c"])

    print(a + b)

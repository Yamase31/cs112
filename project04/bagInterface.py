"""
Author: James Lawson, Harry Pinkerton, Laurie Jones
File: baginterface.py

Speficitactions of the methods for all bag classes.  Running this code will
not produce any results, but it shows the headers and docstrings of the methods
that MUST be included or supported in any bag class.
"""

class BagInterface(object):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        self._modCount = 0

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
        #pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        if len(self) == 0:
            return True
        else:
            return False
        
    def count(self, target):
        """Returns the number of a specific items in self."""
        """ Returns the number of instances of item in self"""
        itemCount = 0
        for nextItem in self:
            if nextItem == target:
                itemCount += 1
        return itemCount
    
    def __len__(self):
        """-Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ",".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)

        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        self._items = Node(item, self._items)
        self._size += 1 
        pass

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        pass

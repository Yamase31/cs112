from abstractCollection import AbstractCollection
from arrays import Array

class AbstractBag(AbstractCollection):
    
    # Class variables
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        super().__init__(sourceCollection)
        
    #Acessor Methods
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
        if half > AbstractBag.DEFAULT_CAPACITY:
            for i in range(len(self)):
                halfArray[i] = self._items[i]
            self._items = halfArray
        else:
            pass
                






        

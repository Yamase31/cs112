class AbstractBag(object):


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""

        self._size = 0
        self._modCount = 0

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size
    
    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        result = type(self)(self)

        for item in other:
            result.add(item)

        return result

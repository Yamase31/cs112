"""
File: abstractDict.py

Authors: Laurie Jones, Harry Pinkerton, James Lawson
Project: 11

Common data and method implementations for dictionaries.
"""
from ..abstractCollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """Represents an abstract dictionary."""

    # Exercise
    def __init__(self, keys, values):
        """Initialize the collection."""
        super().__init__(None)
        
        if keys:
            valueIter = iter(values)
            for key in keys:
                self[key] = next(valueIter)

    def __str__(self):
        return " {" + ", ".join(map(lambda entry: str(entry.key) + \
               ": " + str(entry.value), self.entries())) + "}"

    def get(self, key, defaultValue = None):
        """Returns the associated value if the key is in the
        dictionary, or returns the default value otherwise."""
        if self._getEntry(key) == None:
            return defaultValue
        else:
            return self._getEntry(key).value
   
    def add(self, entry):
        """Adds the values contained in an Entry parameter to the current dictionary."""
        self[entry.key] = entry.value
        
    # Exercise
    def keys(self):
        """Returns an iterator on the keys in the dictionary."""
        keysList = list()
        for key in self:
            keysList.append(key)
        return iter(keysList)

    # Exercise
    def values(self):
        """Returns an iterator on the values in the dictionary."""
        valuesList = list()
        for values in self:
            valuesList.append(self.get(values))
        return iter(valuesList)

    # Exercise
    def entries(self):
        """Returns a iterator on the entries in the dictionary."""
        entriesList = list()
        for entries in self:
            entriesList.append(self._getEntry(entries))
        return iter(entriesList)

    # Exercise
    def __add__(self, other):
        """Returns a dictionary containing the entries of self and
        otherDict.  When keys are equal, the value in otherDict replaces
        the value in self."""
        newDict = type(self)()
        for entry in self.entries():
            newDict.add(entry)
        for entry in other.entries():
            newDict.add(entry)  
        return newDict

    # Exercise
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self == other:
           return True
        else:
            return False

    def _getEntry(self, key):
        """Helper method to obtain the entry rather than the value associated with a key."""
        raise NotImplementedError("Abstract class method invoked!")
    
class Entry(object):
    """Represents a dictionary entry.  Supports comparisons by key."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key

    def __hash__(self):
        return hash(self.key)

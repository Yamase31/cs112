
"""
File: arraySortedBag.py
Author: James Lawson, Harrison Pinkerton, Laruie Jones
A tester program for bag implementations.
"""

from arrays import Array
from abstractBag import AbstractBag
import numpy

class ArraySortedBag(AbstractBag):
    """An array-based bag implementation."""

    turn = 0
    Score1 = 0
    Score2 = 0

    # Class variables
    DEFAULT_CAPACITY = 25

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    def __contains__ (self, item):
        """ implements a more efficient search algorithm"""
        #write this
        for self in self._items:
            if self == item:
                return True
        return False

##########################################################

    # Accessor Methods
    def __iter__(self):
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[cursor]
            if myModCount != self._modCount:
                raise AttributeError("Cannot modify!")
            cursor += 1

    def scoreWord(self, score):
        '''keeps track of the word from each round and the score that it
        contains'''
        
        word1 = {}
        word2 = {}
        
        if self.turn % 2 == 0:
            self.userWord = input("Player 1> ")
            ArraySortedBag.checkWord(self.userWord)
            word1 += self.userWord
            
        else:
            self.userWord = input("Player 2> ")
            ArraySortedBag.checkWord(self.userWord)
            word2 += self.userWord
        
        if self.score != -1:
            print ("You scored", self.score, "points!")
        else:
            print ("you cant spell that word")
        self.turn += 1


    def scorePlayer(self, score):
        '''adds the score of each player to their respective stacks to
        be displayed at the end'''
        Score1 = {}
        Score2 = {}
        
        
        self.turn = 0
            
        print("Avaliable letters: ", self._items)
        print(self.turn)
        print("score:", score)
        #print("player 1 tot:", b.scorePlayer())
        
        if self.turn % 2 == 0:
            self.userWord = input("Player 1> ")
            ArraySortedBag.checkWord(self.userWord)
            Score1 += self.score
            
        else:
            self.userWord = input("Player 2> ")
            ArraySortedBag.checkWord(self.userWord)
            Score2 += self.score
                
    def checkWord(self, word):
        
        score = 0
        self.turn = 0
        for i in word:
            if self.__contains__(i) is True:
                #self.remove(i)
                score += 1
            else:
                score = -1
            
            if i == len(self._items):
                score = -1
            
        #self.remove(i)
        return score
            
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
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True


############################################################
    # Mutator Methods

    def generate(self, v,c):
        
        self.clear()
        
        vowels = ["a", "e", "i", "o", "u"]
        consonants = ["b", "c", "d", "f", "g", "h", "j", "k" ,"l" ,"m" ,"n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        
        
        for i in range(v):
            self.add(numpy.random.choice(vowels))

        for i in range(c):
           self.add(numpy.random.choice(consonants))

        
    
    def clear(self):
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        self._modCount += 1
        

    def add(self, item):
        # resize here if needed

        #print(self._items)
        
        if len(self._items) == len(self):
            self.grow()

        newIndex = len(self)

        for i in range(len(self)):
            if item <= self._items[i]:
                newIndex = i
                break
            
        for j in range(len(self), newIndex, -1):
            self._items[j] = self._items[j -1]
        self._items[newIndex] = item
        self._size += 1


    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        tIndex = 0
        for i in range(len(self._items)):
            if item == self._items[i]:
                tIndex = i
                break
            if i == len(self)+1:
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
        if half > ArraySortedBag.DEFAULT_CAPACITY:
            for i in range(len(self)):
                halfArray[i] = self._items[i]
            self._items = halfArray
        else:
            pass



def main():
    
    b = ArraySortedBag()
    b.generate(10, 15)
    userWord = input("press enter to start game!")
    score = b.checkWord(userWord)
    
    
    while score >= 0:
        b.scorePlayer(score)
        b.scoreWord(score)

        
        

        





if __name__ == "__main__":
    main()

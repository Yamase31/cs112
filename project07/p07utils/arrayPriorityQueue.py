#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:26:45 2019

@author: hannahjones
"""


from .arrayQueue import ArrayQueue

class ArrayPriorityQueue(ArrayQueue):
    
        # Constructor 
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)
        


    # Mutator methods
    def add(self, item):
#If the queue is empty, or the new item >= the rear item
        if len(self) == len(self._items):
            super().grow()
            
        if self.isEmpty() or item >= self._items[self._rear]:
            super().add(item)
            
    #If the item is < the first item in the queue
        elif item < self._items[self._front]:
            self._size += 1
            self.incModCount()
            
            self._front -= 1
            self._front %= len(self._items)
            self._items[self._front]= item
            
    #Otherwise Use a probe to search for the first item > the new item
        else:
            if len(self)== len(self._items):
                self.grow()
            index = self._size
            while index > 0:
                if self._items[(index -1 + self._front) % len(self._items)] > item:
                    self._items[(index + self._front) % len(self._items)] = self._items[(index - 1 + self._front)% len(self._items)]
                    index -= 1
                else:
                    break
            self._items[(index + self._front) % len(self._items)] = item
            
            self._size += 1
            self._rear += 1
            self._rear %= len(self._items)
    
        #print(self._items)
    
    
    
    
    
    
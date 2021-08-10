#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:07:10 2019

@author: hannahjones
"""

from .node import Node
#from .abstractCollection import AbstractCollection
from .linkedQueue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):
    
    def __init__ (self, sourceCollection = None):
        super().__init__(sourceCollection)
    
    def add(self, item):
        newNode = Node(item)
        
    #If the queue is empty, or the new item >= the rear item
        if self.isEmpty() or item >= self._rear.data:
            super().add(item)
            
    #If the item is < the first item in the queue
        elif item < self._front.data:
            self._size += 1
            self.incModCount()
            newNode = Node(item, self._front)
            self._front = newNode
            
    #Otherwise Use a probe to search for the first item > the new item
        else:
            pointer = self._front
            self._size += 1
            self.incModCount()
            
            while pointer.next.data <= item:
                pointer = pointer.next
            newNode = Node(item, pointer.next)
            pointer.next = newNode
            
                
            
            
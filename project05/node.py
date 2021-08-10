"""
Author: Harry Pinkerton, James Lawson, Laurie Jones
File: node.py
Project: 5
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

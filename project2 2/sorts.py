"""
Author: James Lawson, Harry Pinkerton, Hannah Jones
File: sorts.py

Defines selection sort, quick sort, insertion sort, all of which iterate through
a list and organize a list.
"""
from counter import Counter
from tools import getRandomList

def selectionSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a selection sort."""
  
    n = len(lyst)
    for i in range(n):
      minIndex = minInRange(lyst,i,n, comps)
      if comps:
         comps.increment() 
      if minIndex != i:
         if swaps:
            swaps.increment() 
         swap(lyst, i, minIndex)

def quickSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a quick sort."""
    def recurse(lyst, left, right, comps, swaps):
      if comps:
         comps.increment() 
      if left < right:
         pivotPos = partition(lyst, left, right, comps, swaps)
         recurse(lyst, left, pivotPos - 1, comps, swaps);
         recurse(lyst, pivotPos + 1, right, comps, swaps)
         
    def partition(lyst, left, right, comps, swaps):
      # Find the pivot and exchange it
      #  with the last item
      middle = (left + right) // 2
      pivot = lyst[middle]
      lyst[middle] = lyst[right]
      lyst[right] = pivot

      # Set boundary point to first position
      boundary = left

      # Move items less than pivot to the left
      for index in range(left, right):
          if comps:
              comps.increment()
          if lyst[index] < pivot:
              if swaps:
                 swaps.increment() 
              swap(lyst, index, boundary)
              boundary += 1
        # Exchange the pivot item and 
        # The boundary item


      swap(lyst, right, boundary)
      return boundary
    recurse(lyst, 0, len(lyst) - 1, comps, swaps)
      


def minInRange(lyst, i, n, comps):
   minValue = lyst[i]
   minIndex = i
   for j in range(i, n):
      if comps:
         comps.increment() 
      if lyst[j] < minValue:
         minValue = lyst[j]
         minIndex = j
   return minIndex

def swap(lyst, i, j, counter = None):
    """Exchanges the items at i and j in lyst and increments
    the counter if it exists."""
    if counter: counter.increment()
    lyst[i], lyst[j] = lyst[j], lyst[i]       

def test(sort, n = 15):
    """Runs some tests on a sort function."""
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)

def testWithCounters(sort, n = 15):
    """Runs some tests on a sort function."""
    comps = Counter()
    swaps = Counter()
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))
    comps.reset()
    swaps.reset()
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))

def insertionSort(comps = None, swaps = None):
    for item in range(i):
        i = 1
        if item[i-1] > i:
            item[i-1] = item[i+1]
            comps += 1
            swaps += 1
        if item[i-1] <= i:
            i = i
            comps += 1

def main():
    """To test, pass the name of the sort function to test."""
    test(selectionSort)
    testWithCounters(selectionSort)
    testWithCounters(selectionSort, n = 15)
    test(quickSort)
    testWithCounters(quickSort, n = 15)

if __name__ == "__main__":
    main()

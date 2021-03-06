"""
Author: edited by Harry Pinkerton, Laurie Jones, James Jawson
File: nQueens.py
Project 1

This code creates a board that has a "n" number of queens that are in safe positions based off the of rules of chess.
It also compares the two different ways of goign through the board, one efficiently, (nQueensFancy) and inefficiently
(nQueensBrute). 

"""


import time

def nQueensFancy(n=8):
   # Set up the board with all the queens in row 0
   board = [0 for x in range(n)]
   currentQueen = 0

   # Check the current queen against all previously safely placed queens
   # If the current queen is safe, move on to the next queen
   # If the current queen is not safe and the current queen can move down in their column, move the queen
   while(currentQueen <= len(board) - 1):
      if safeQueen(board, currentQueen):
         currentQueen += 1
   #If the current queen is not safe and cannot move in the column, backtrack through the safe
   # queens until a queen can move
      else:
         while(board[currentQueen] >= len(board) -1):
            board[currentQueen] = 0
            currentQueen -= 1
         board[currentQueen] += 1
   return board


def nQueensBrute(n=8):
   # Set up the board with all the queens in row 0
   board = [0 for x in range(n)]
   
   # Continue to move queens until the board is safe
   while(not(safeBoard(board))):
      # There's at least one overflow if we're in this loop, start with the first queen
      overflow = True
      currentQueen = len(board) - 1
      
      # While we need to move queens, move them and check for overflow
      while(overflow):
         board[currentQueen] += 1
         
         # If the queen we moved has fallen off the board, we overflow to the next queen
         if board[currentQueen] == len(board):
            board[currentQueen] = 0
            currentQueen -= 1
         
         # Otherwise we can stop moving queens
         else:
            overflow = False
            
   # We've hit the end, we can print a solution!
   return board


def printBoard(board):
   
   if board == None:
      return
   
   # Print the top border
   print("----" * len(board) + "-")
   
   # Iterate through the board and print Q if we have a queen there
   for row in range(len(board)):
      print("| ", end="")
      for col in range(len(board)):
         if board[col] == row:
            print("Q | ", end="")
         else:
            print("  | ", end="")
      
      # Print a line between the queens
      print()
      print("----" * len(board) + "-")
      

def safeBoard(board):
   # Check all queens to be safe, return false if not safe
   
   for colQ1 in range(len(board)):
      for colQ2 in range(colQ1+1,len(board)):
         if checkHorizontal(board[colQ1], board[colQ2]) or checkDiagonal(board[colQ1], colQ1, board[colQ2], colQ2):
            return False
         
   return True


def safeQueen(board, colQ1):
   # Check all queens to the left of current queen to make sure that current queen is safe
   for colQ2 in range(colQ1):
      if checkHorizontal(board[colQ1], board[colQ2]) or checkDiagonal(board[colQ1], colQ1, board[colQ2], colQ2):
         return False

   return True


   
def checkHorizontal(rowQ1, rowQ2):
   # Return if two queens on horizontal
   return rowQ1 == rowQ2

def checkDiagonal(rowQ1, colQ1, rowQ2, colQ2):
   # return if two queens on diagonal
   diffRow = abs(rowQ1 - rowQ2)
   diffCol = abs(colQ1 - colQ2)
   
   return diffRow == diffCol
   

def main():
   
   number = int(input("Enter the size of the board: "))
   if number >= 4:
      
      start = time.time()
      bruteBoard = nQueensBrute(number)
      end = time.time()
      bruteElapsed = end - start
      
      start = time.time()
      fancyBoard = nQueensFancy(number)
      end = time.time()
      fancyElapsed = end - start
      
      
      print("N Queens brute force time elapsed: %.10f" % (bruteElapsed))
      print("N Queens fancy style time elapsed: %.10f" % (fancyElapsed))
      
      print("\nBrute Force")
      printBoard(bruteBoard)
      
      print("\nFancy")
      printBoard(fancyBoard)
      
      
   else:
      print("Number too small!")
   



if __name__ == '__main__':
   main()

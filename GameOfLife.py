# python 2
#
# Game of Life
#
# Name: Matt

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoardFake(width, height):
    for i in range(height):
        print width*"0"
    """
    prints zeroes with length width, and height of rows
    """
#createBoardFake(5, 4)


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]    # What do you need to add a whole row here?
    return A
#print createBoard(10,5)


def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line
A = createBoard(10,10)
#printBoard(A)


def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A
A = diagonalize(7,7)
#print A
#printBoard(A)


def innerCells(w, h):
    A = createBoard(w, h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = 1
    return A
A = innerCells(10,10)
#printBoard(A)


def randomCells(w,h):
    A = createBoard(w, h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = random.choice([0,1])
    return A
A = randomCells(10,8)
#printBoard(A)


def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]
    return newA
A = randomCells(5,5)
#printBoard(A)


def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA
A = randomCells(10,5)
printBoard(A)
print " "
A = innerReverse(A)
printBoard(A)


def countNeighbors(row, col, A):


def next_life_generation(A):
    

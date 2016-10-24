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
A = createBoard(5,3)
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
A = diagonalize(7,6)
print A

printBoard(A)

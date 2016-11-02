import random


def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

"""
def createBoardFake(width, height):
    for i in range(height):
        #print width*"0"

    #prints zeroes with length width, and height of rows

#createBoardFake(5, 4)
"""

def createBoard(width, height):
    #returns a 2d array with "height" rows and "width" cols
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



def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]
    return newA
#A = randomCells(5,5)
#printBoard(A)




def countNeighbors(row, col, A):
    NeighborCount = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            NeighborCount = NeighborCount + A[r][c]
    NeighborCount -= A[row][col]
    return NeighborCount
"""
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]

printBoard(A)
print countNeighbors(2,1,A)
print countNeighbors(2,2,A)
print countNeighbors(0,1,A)
"""
"""
def next_life_generation(A):
    newA=copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(1,height-1):
        for col in range(1,width-1):
            neighborCount = countNeighbors(row, col, A)
            if neighborCount > 3:
                newA[row][col] = 0
            elif neighborCount < 2:
                newA[row][col] = 0
            elif neighborCount == 3:
                newA[row][col] = 1
    return newA

A = randomCells(10,10)
printBoard(A)
for x in range(10):
    A = next_life_generation(A)
    printBoard(A)
    print " "
"""

def unsegregatedBoard(width, height, percentX, percentY):
    numberX = int(width*height*percentX)
    numberY = int(width*height*percentY)
    number0 = (width*height)-numberX-numberY
    population = numberX*'X' + numberY*'Y' + number0*'0'
    population = random.sample(population, width*height)

    heya = 0
    Z = createBoard(width, height)
    for row in range(width):
        for col in range(height):
            Z[row][col] = population[heya]
            heya = heya +1
    return Z

Z = unsegregatedBoard(10,10,.4,.4)
printBoard(Z)

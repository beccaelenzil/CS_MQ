#CONNECT FOUR GAME

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """

        self.width = width
        self.height = height

        W = self.width
        H = self.height

        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        W = self.width
        H = self.height

        s = ''   # the string to return
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'

        x = -1
        for i in range(W):
            if x == 9:
                x = 0
                s += " " +str(x)
            else:
                x+= 1
                s += " " + str(x)

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        counter = 0
        PC = ox
        try_row = self.height -1
        movePosition = self.data[try_row][col]

        while movePosition != ' ':
            try_row += -1
            movePosition = self.data[try_row][col]
        if movePosition == ' ':
            self.data[try_row][col] = PC


    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, col):
        if col >= self.width or col <0:
            return False
        elif self.data[0][col] != ' ':
            return True
        else:
            return False


    def isFull(self):
        full = True
        for col in range(self.width):
            for row in range(self.height):
                if self.data[col][row] == ' ':
                    full = False

        return full

    def delMove(self, col):
        try_row = 0
        movePosition = self.data[try_row][col]

        while movePosition == ' ':
            try_row += 1
            movePosition = self.data[try_row][col]
        if movePosition != ' ':
            self.data[try_row][col] = ' '

    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True
                elif D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True







boardy = Board(6,7)
boardy.setBoard('00102030')
print boardy

print boardy.winsFor('X')



"""
boardy.addMove(3, 'X')

boardy.addMove(4, 'O')

boardy.addMove(3, 'X')

boardy.addMove(3, 'O')
"""






"""
print boardy.allowsMove(-1)

print boardy.allowsMove(0)

print boardy.allowsMove(1)

print boardy.allowsMove(2)

print " "
print boardy.isFull()
"""


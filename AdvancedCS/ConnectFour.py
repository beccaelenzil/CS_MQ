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
        try_row = self.height -1
        out_of_range = False
        movePosition = self.data[try_row][col]
        done = False

        if col > -1 and col < self.width:
            movePosition = self.data[try_row][col]


        """
        this function will start with a while loop to check if the move stacking will work,
        or be out of range. I use out_of_range variable to make sure that the while loop does
        not run forever. the following if elif statements check if the column input is out of the
        domain of the defined board.
        """

        if col < 0:
            print False
            done = True

        elif col > self.width:
            print False
            done = True

        while movePosition != ' ' and out_of_range == False and done == False:
            if try_row > -1:
                try_row += -1
                movePosition = self.data[try_row][col]
            elif try_row < 0:
                print False
                out_of_range = True

        if movePosition == ' ' and done == False:
            print True


    #def isFull(self):


boardy = Board(2,2)

#print boardy

"""
boardy.addMove(3, 'X')

boardy.addMove(4, 'O')

boardy.addMove(3, 'X')

boardy.addMove(3, 'O')
"""

boardy.addMove(0, 'X')

boardy.addMove(0, 'O')



print boardy

boardy.allowsMove(-1)

boardy.allowsMove(0)

boardy.allowsMove(1)

boardy.allowsMove(2)

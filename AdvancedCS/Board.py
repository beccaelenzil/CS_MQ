#CONNECT FOUR GAME
# File: Board.py
# Verions: Python 2.7.13
# Name: Matt Querdasi
# Date: 3/21/17
# Desc: PROG DESC
# Usage: Board class for connect four game

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

    #adds move to lowest free space in a column
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

    #sets board given specific string
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

    #checks if the move is within domain, and if there are already pieces
    def allowsMove(self, col):
        if col >= self.width or col <0:
            return False
        elif self.data[0][col] != ' ':
            return False
        else:
            return True

    #checks if the board is full, default is True
    def isFull(self):
        full = True
        for col in range(self.width):
            for row in range(self.height):
                if self.data[row][col] == ' ':
                    full = False

        return full

    #deletes the highest move in a column
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
        win = False
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    win = True
        #check for vertical wins
        for col in range(0, W):
            for row in range(0, H-3):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    win = True
        #check for diagonal wins down
        for row in range(0, H-3):
            for col in range(0, W-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+3][col+3] == ox:
                    win = True
        #check for diagonal wins up
        for row in range(3, H):
            for col in range(0, W-3):
                if D[row][col] == ox and \
                   D[row-1][col+1] == ox and \
                   D[row-2][col+2] == ox and \
                   D[row-3][col+3] == ox:
                    win = True

        return win

    def hostGame(self):
        gameOver = False

        print "Hello and welcome to connect 4, oldies edition"

        while gameOver == False:

            players = ['X', 'O']

            """
            sets up a while loop containing two player options, alternates between players. Takes an
            input and checks using allow move if move works. if move does not work, input is prompted.
            Then adds move after while loop. If statements check for win, full, and then last if
            statement ends method.
            """

            for i in players:
                print self.__repr__()
                print ' '

                moveChoice = -1

                moveChoice = input('What column would ' + i + ' like to choose? ')

                while self.allowsMove(moveChoice) == False:
                    print
                    moveChoice = input('That is not a valid choice, ' + i + ' what is your choice? ')

                self.addMove(moveChoice, i)

                if self.winsFor(i) == True:
                    print self.__repr__()
                    print ' '
                    print i + ' wins!'
                    gameOver = True
                if self.isFull() == True:
                    print ' '
                    print 'The board is full, please restart'
                    gameOver = True
                if gameOver == True:
                    break




#b= Board(7,6)
#b.hostGame()

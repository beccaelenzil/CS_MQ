from Board import Board

class Player():
    """ an AI for connect four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    #returns opposing player
    def oppCh(self):
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'

    def scoreBoard(self, b):
        score = 0.0
        if b.winsFor(self.ox, ):
            score = 100.0
        elif b.winsFor(self.oppCh()):
            score = 0.0
        else:
            score = 50.0
        return score

    def tiebreakMove(self, scores):

        max(scores)


b = Board(7,6)
b.setBoard( '01020305' )
print b

p = Player( 'X', 'LEFT', 0 )
print p.scoreBoard(b)

print Player('O', 'LEFT', 0).scoreBoard(b)


print Player('O', 'LEFT', 0).scoreBoard(Board(7,6))


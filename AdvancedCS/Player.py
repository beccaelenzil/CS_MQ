import random
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

    #takes in scores list and returns column number of highest scores resulting from possible moves
    def tiebreakMove(self, scores):
        maxIndices = []  #list with scores

        for i in range(len(scores)):  #goes through list for how many scores there are
            if scores[i] == max(scores):  #finds highest scores and appends to maxIndices
                maxIndices.append(i)

        #taking tie break type and implementing left or right move, if only there is more than one high score
        if len(maxIndices) > 1:
            if self.tbt == 'RIGHT':
                return maxIndices[len(maxIndices)-1]
            elif self.tbt == 'LEFT':
                return maxIndices[0]
            else:
                return maxIndices[random.randrange(len(maxIndices))]
        else:
            return maxIndices[0]


    def scoresFor(self, b):
        scores = []

        for col in range(b.width):
            b.addMove(col, self.ox)
            if b.allowsMove(col):
                if self.scoreBoard(b) == 100.0:
                    scores.append(self.scoreBoard(b))
                else:
                    b.addMove(col, self.oppCh())
                    scores.append(self.scoreBoard(b))
                    b.delMove(col)
            else:
                scores.append(-1)
            b.delMove(col)

        for col in range(b.width):
            b.addMove(col, self.oppCh())
            if scores[col] == 50.0:
                scores[col] = self.scoreBoard(b)
            b.delMove(col)

        return scores


b = Board(7,6)
b.setBoard( '01020305' )
print b

p = Player( 'X', 'LEFT', 0 )
print p.scoreBoard(b)

print Player('O', 'LEFT', 0).scoreBoard(b)


print Player('O', 'LEFT', 0).scoreBoard(Board(7,6))


scores = [0, 0, 50, 0, 50, 50, 0]
p = Player('X', 'LEFT', 1)
p2 = Player('X', 'RIGHT', 1)
print p.tiebreakMove(scores)

print p2.tiebreakMove(scores)

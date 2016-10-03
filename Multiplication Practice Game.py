import random


def play():
    userAnswer = 145
    correctAnswer = 146
    gameCount = 0
    score = 0
    for gameCount in range(0,5):
        if userAnswer != correctAnswer or userAnswer == correctAnswer:
            factor1 = random.randint(0,12)
            factor2 = random.randint(0,12)
            userAnswer = raw_input('Please enter the product of ' + str(factor1) + ' and ' + str(factor2))
            correctAnswer = factor1 * factor2
            userAnswer = int(userAnswer)
            if userAnswer == (factor1*factor2):
                score = score + 1
                print ('Correct!')
                gameCount = gameCount + 1
                print gameCount
            else:
                score = score - 2
                print ('Wrong!')
                print ('Try again!')
                gameCount = gameCount + 1
                print gameCount
    print 'Your total score is ' + str(score)
def instructions():
    print 'Hey there sailor!'
    print 'Every correct answer gets you 1 point'
    print 'Every incorrect answer gets you -2 points'
    print ' '
def endScore():
    print 'Nice job!'
def main():
    instructions()
    play()
    endScore()
main()
# GET HELP ON MAKING THE SCORE PRINT AT THE END!!!!!!!!*********

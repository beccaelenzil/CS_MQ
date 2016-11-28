import random

#My enhancement is to create a scoring system that tells you how well you did at the end
def play():
    userAnswer = 145
    correctAnswer = 146
    gameCount = 0
    score = 0
    for gameCount in range(0,5):
        if userAnswer != correctAnswer or userAnswer == correctAnswer:
            factor1 = random.randint(0,12)
            factor2 = random.randint(0,12)
            userAnswer = raw_input('Please enter the product of ' + str(factor1) + ' and ' + str(factor2) + ' ')
            correctAnswer = factor1 * factor2
            while userAnswer.isdigit() == False:
                print 'Please input a numerical value'
                print ' '
                userAnswer = raw_input('Please enter the product of ' + str(factor1) + ' and ' + str(factor2) + ' ')
            userAnswer = int(userAnswer)
            if userAnswer == (factor1*factor2):
                score = score + 1
                print ('Correct!')
                print ' '
                gameCount = gameCount + 1
            else:
                score = score - 2
                print ('Wrong!')
                print ('Try again!')
                print ' '
                gameCount = gameCount + 1
    return score
def instructions():
    print 'Hey there sailor!'
    print 'Every correct answer gets you 1 point'
    print 'Every incorrect answer gets you -2 points'
    print 'You have five tries to get the highest score'
    print 'Good luck!'
    print ' '
def endScore(score):
    print 'Nice job!'
    print 'Your total score is ' + str(score)
def main():
    instructions()
    score = play()
    endScore(score)
main()
# GET HELP ON MAKING THE SCORE PRINT AT THE END!!!!!!!!*********

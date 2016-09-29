import random

factor1 = random.randint(0,12)
factor2 = random.randint(0,12)

def play():
    userAnswer = 145
    correctAnswer = 146
    score = 0
    while userAnswer != correctAnswer:
        userAnswer = raw_input('Please enter the product of ' + str(factor1) + ' and ' + str(factor2))
        correctAnswer = factor1 * factor2
        userAnswer = int(userAnswer)
        if userAnswer == (factor1*factor2):
            print ('Correct!')
        else:
            print ('Wrong!')
            print ('Try again!')
def instructions():
    print 'Hey there sailor!'
    print 'Every correct answer gets you 1 point'
    print 'Every incorrect answer gets you -2 points'
    print ' '
def main():
    instructions()
    play()
main()

import random

def play():
    gamecount = 0
    GITnumber = random.randint(1,100)
    userAnswer = 103
    correctAnswer = GITnumber
    while userAnswer != correctAnswer:

        userAnswer = (raw_input('Whats your guess? '))

        #check for valid input
        while userAnswer.isdigit() == False:
            print 'Please input a numerical value'
            print ' '
            userAnswer = (raw_input('Whats your guess? '))

        userAnswer = int(userAnswer)

        #checking if it's too high, too low, or correct
        if userAnswer < 0:
            print 'Remember, your number has to be within 1 and 100'
            print ' '
        elif userAnswer > 100:
            print 'Remember, your number has to be within 1 and 100'
            print ' '
        #elif userAnswer != #NEED TO MAKE SO IT GIVES ERROR IF YOU DON't PUT A NUMBER IN
        else:
            if userAnswer == correctAnswer:
                print 'You guessed it. Nice job!'
                print ' '
                gamecount = gamecount + 1
            elif userAnswer < correctAnswer:
                print 'Too low!'
                print ' '
                gamecount = gamecount + 1
            elif userAnswer > correctAnswer:
                print 'Too high!'
                print ' '
                gamecount = gamecount + 1
    return gamecount
def instructions():
    print 'Hello and welcome to Guess My Number!'
    print 'Please guess a number between 0 and 100'
    print ' '

def endStuff(gamecount):
    print 'That took you ' + str(gamecount) + ' tries'

def main():
    instructions()
    gamecount = play()
    endStuff(gamecount)

main()

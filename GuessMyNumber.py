import random

def play():
    gamecount = 0
    GITnumber = random.randint(1,101)
    userAnswer = 103
    correctAnswer = GITnumber
    while userAnswer != correctAnswer:
        if userAnswer != correctAnswer:
            userAnswer = int(raw_input('Whats your guess? '))
            if userAnswer < 0:
                print 'Remember, your number has to be within 1 and 100'
                print ' '
            elif userAnswer > 100:
                print 'Remember, your number has to be within 1 and 100'
                print ' '
            elif userAnswer != #NEED TO MAKE SO IT GIVES ERROR IF YOU DON't PUT A NUMBER IN
            else:
                if userAnswer == correctAnswer:
                    print 'You guessed it. Nice job!'
                    print ' '
                elif userAnswer < correctAnswer:
                    print 'Too low!'
                    print ' '
                elif userAnswer > correctAnswer:
                    print 'Too high!'
                    print ' '

def instructions():
    print 'Hello and welcome to Guess My Number!'
    print 'Please guess a number between 0 and 100'
    print ' '

def endStuff():
    print 'That took you'

def main():
    instructions()
    play()
    endStuff()

main()

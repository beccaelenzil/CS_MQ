import random


Slope = random.randint(0,10)
yIntercept = random.randint(0,10)

def play():
    x = raw_input("please select a number: ")
    compRule = Slope*int(x)+yIntercept
    print 'm('+str(int(x))+')+'+'b= '+str(compRule)
    y = raw_input('Do you need another guess? ')
    if y == 'yes':
        play()
    elif y == 'no':
        GuessRule()

def GuessRule():
    z = raw_input('What do you think m is? ')
    if int(z) == Slope:
        print 'Good job!'
        q = raw_input('What do you think b is? ')
        if int(q) == yIntercept:
            print 'You win!'
    else:
        print 'Nope'
        print 'Try more numbers'
        play()


def instructions():
    print "hi! Let's play a game."
    print "I'm thinking of two numbers, each between 1 and 10"
    print "You give me a number, and then try to guess my numbers."
    print "I'll multiply your number my first number, and then add my second number to the product."
    print "(My 1st number * your number)+ my 2nd number"
    print "Then, I'll ask if you need more guesses. You can try as many numbers as you want."
    print "When you think you know my numbers, tell me you don't need more guesses by typing 'no' and you can try to guess them."
    print " "
    play()


instructions()







#OLD CODE BEFORE COLLABORATION
"""
import random

aValue = random.randint(1,5)
bValue = random.randint(1,5)
def play():
    userValue = raw_input('Please input a sample value for the mystery rule ')
    x = int(userValue)
    ruleOutput = (aValue * int(userValue)) + bValue
    print 'm*' + str(userValue) + ' + ' + 'b' + ' = ' + str(ruleOutput)
    print ' '
    guessYesOrNo = raw_input('Would you like to guess to guess m and b values? ')
play()


def instructions():
    print 'Hello!'
    print 'Welcome to Guess my Rule Game (by Matt and Colin)'

def endGame():


def main():
    instructions()
    play()
    endGame()

main()
"""

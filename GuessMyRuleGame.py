import random

aValue = random.randint(1,5)
bValue = random.randint(1,5)
def play():
    userValue = raw_input('Please input a sample value for the mystery rule ')
    x = int(userValue)
    ruleOutput = (aValue * int(userValue)) + bValue
    print 'm*' + str(userValue) + ' + ' + 'b' + ' = ' + str(ruleOutput)

play()

"""
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

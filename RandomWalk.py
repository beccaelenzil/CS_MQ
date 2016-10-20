import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])


def rwpos(start, nsteps):
    currentPosition = start
    for i in range(0, nsteps):
        currentPosition = currentPosition + rs()
        #print 'Current position is ' + str(currentPosition)
    return currentPosition
#print rwpos(20, 7)


def rwsteps(start, low, hi):
    currentPosition = start
    geigerCounter = 0
    left_spaces = low + start
    right_spaces = hi - start
    print '|' + left_spaces*' ' + 'X' + right_spaces*' ' + '|'+str(currentPosition)
    while currentPosition in range(low+1, hi):
        currentStep = rs()
        currentPosition = currentPosition + currentStep
        geigerCounter = geigerCounter + 1
        if currentStep == 1:
            right_spaces = right_spaces - 1
            left_spaces = left_spaces + 1
        else:
            right_spaces = right_spaces + 1
            left_spaces = left_spaces - 1
        print '|' + left_spaces*' ' + 'X' + right_spaces*' ' + '|'+str(currentPosition)
    print 'That took ' + str(geigerCounter) + ' steps'
    return currentPosition
#print rwsteps(5,0,10)


def rwposPlain(start, nsteps):
    currentPosition = start
    for i in range(0, nsteps):
        currentPosition = currentPosition + rs()
    return currentPosition
#print rwpos(20, 7)


def ave_signed_displacement(numtrials):
    total = 0
    for i in range(numtrials):
        total = total + rwposPlain(0,100)
    actualTotal = total/numtrials
    return actualTotal
print ave_signed_displacement(3)

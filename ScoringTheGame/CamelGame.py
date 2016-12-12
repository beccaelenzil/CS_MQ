import random

def instructions():
    print 'Welcome to Camel!'
    print 'You have stolen a camel to make your way across the great Mobi desert.'
    print 'The natives want their camel back and are chasing you down! Survive your'
    print 'desert trek and outrun the natives.'

def camellinAlong():
    done = False
    distanceTraveled = 0
    thirstiness = 5
    camelTiredness = 0
    nativesDistance = 10
    oasisChance = random.randint(0,19)
    distanceLeft = 200
    drinksRemaining = 3


    while done == False:
        if distanceLeft > 0:
            print ' '
            print 'A. Drink from your canteen.'
            print 'B. Ahead moderate speed.'
            print 'C. Ahead full speed.'
            print 'D. Stop and rest.'
            print 'E. Status check.'
            print 'Q. Quit.'
            x = raw_input('Select an option: A, B, C, D, E, Q:')
            x = x.upper()
            print ' '
        if oasisChance == 5:
            print 'YOU FOUND AN OASIS!'
            print 'You found 3 more drinks!'
            drinksRemaining += 3

        if distanceLeft < 1:
            print 'You made it to the end'
            print 'You win!'
            playAgain()

        if x == 'A':
            if drinksRemaining > 0:
                thirstiness = thirstiness - 5
                nativesDistance -= random.randint(12,24)
                thirstiness -= random.randint(5,15)
                drinksRemaining -= 1
                print 'Boom. Hydrated.'
                print 'You have ' + str(drinksRemaining) + ' drinks left'
            elif drinksRemaining < 1:
                print 'You have no more drinks. Please select a different option.'

        elif x == 'B':
            distanceB = random.randint(7,12)
            distanceLeft -= distanceB
            distanceTraveled += 10
            thirstiness += random.randint(1,4)
            nativesDistance += distanceB
            camelTiredness += random.randint(1,4)
            if distanceLeft > 0:
                print 'You traveled ' + str(distanceB) + ' miles'
                print 'You have ' + str(distanceLeft) + ' miles to go'

        elif x == 'C':
            distanceC = random.randint(13,18)
            distanceLeft -= distanceC
            distanceTraveled += 20
            thirstiness += random.randint(2,6)
            nativesDistance += distanceC
            camelTiredness += random.randint(3,6)
            if distanceLeft > 0:
                print 'You traveled ' + str(distanceC) + ' miles'
                print 'You have ' + str(distanceLeft) + ' miles to go'

        elif x == 'D':
            camelTiredness -= 15
            nativesDistance -= random.randint(15,30)
            print 'Boom. Camel rejuvenated.'
            print 'You have ' + str(distanceLeft) + ' miles to go'

        elif x == 'E':
            print 'Your status is '

        elif x == 'Q':
            print 'Thanks for playing'


        if nativesDistance < 20:
            if 0 < nativesDistance < 20:
                print 'The natives are getting close!'
            elif nativesDistance < 1:
                print 'The natives caught you!'
                done = True
        if camelTiredness > 10:
            if 19 > camelTiredness > 10 and distanceLeft > 0:
                print 'Your camel is getting tired!'
            elif camelTiredness > 19 and distanceLeft > 0:
                print 'Your camel died!'
                done = True
        if distanceLeft < 1:
            print 'You made it to the end!'
            done = True
        if thirstiness > 10:
            if 19 > thirstiness > 10 and distanceLeft > 0:
                print 'You are getting thirsty!'
            elif thirstiness > 19 and distanceLeft > 0:
                print 'You died from thirst'
                done = True

        if done == True:
            playAgain()

def playAgain():
    print ' '
    a = raw_input('Would you like to play again? Yes or no?')
    if a.upper() == 'YES':
        main()
    elif a.upper() == 'NO':
        print 'Thanks for playing!'
    else:
        print 'Please enter yes or no'
        playAgain()



def main():
    instructions()
    camellinAlong()

main()

artists = []

for i in range(3):
    next_artist = raw_input('Enter an artist that you like:')
    artists.append(next_artist)
print ('Thank you!  Well work on your recommendations now.')


def factorial(n):
    answerSoFar = 1
    for factor in range(1, n+1):
        answerSoFar = answerSoFar * factor
    return answerSoFar
print factorial(4)


def numMatches(listA, listB):
    ''' return the number of elements that match between
        listA and listB '''
    count = 0
    for item in listA:
        if item in listB:
            count += 1
    return count
print numMatches([4,5,6],[5,6,7])


def findBestUser(userPrefs, allUsersPrefs):
    ''' Given a list of user artist preferences and a
        list of lists represented all stored users'
        preferences, return the index of the stored
        user with the most matches to the current user. '''
    max_matches = 0
    best_index = 0
    for i in range(len(allUsersPrefs)):
        curr_matches = countMatches(userPrefs,
                                    allPrefs[i])
        if curr_matches > max_matches:
            best_index = i
            max_matches = curr_matches
    return best_index

"""
newPref = raw_input("Please enter the name of an \
artist or band that you like: " )
while newPref != '':
    prefs.append(newPref)
    newPref = raw_input("Please enter an artist or band \
that you like, or just press enter to see recommendations: ")
print('Thanks for your input!')
NOT WORKING
"""


def factorial(n):
    answer = 1
    while n > 0:
        answer = answer * n
        n = n-1
    return answer


numCorrect = 0
while True:      # run forever -- or at least as long as needed...
    newPref = raw_input("Please enter an artist or band that you like, or just press enter to see recommendations: ")
    if newPref:
        prefs.append(newPref)
    else:
        break
print('Thanks for your input!')


counter = 0
while counter < 10000:
    counter = counter + 1
#ran in 2.6 milliseconds. The "equivalent" recursive program
def increment(value, times):
    if times <= 0:
        return value
    return increment(value + 1, times - 1)
counter = increment(0, 10000)

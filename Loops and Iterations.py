import math

def power(b,p):
    """
    """
    if p == 0:
        return 1
    start = b
    for x in range(1,p):
        b = b*start
    return b
print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)


def summedOdds( L ):
    """ loop-based function to return a numeric list, summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for e in L:
        if e%2==1:
            result = result + e
    return result
# tests!
print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 == ", summedOdds( range(3,10) )


def mult(n,m): #KEEP WORKING ON THIS ONE
    new = 0
    if n<0:
        begin = n
        for x in range(n,0):
            new = new - m
        return new
    elif n>0:
        for x in range(0,n):
            new = new + m
        return new
    elif n == 0 or m == 0:
        return 0
# tests!
print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)


def dot( L,K ):
    result = 0.0
    if len(L) != len(K):
        return 0.0
    else:
        for x in range (0,len(L)):
            result = result + L[x]*K[x]
        return result
print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] )
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )


def count_evens(L):
    evencount = 0
    for x in (L):
        if x % 2 == 1:
            evencount = evencount + 0
        else:
            evencount = evencount + 1
    return evencount
print "count_evens([2, 1, 2, 3, 4], 3 == ", count_evens([2, 1, 2, 3, 4])
print "count_evens([2, 2, 0]), 3 == ", count_evens([2, 2, 0])
print "count_evens([1, 3, 5]), 0 == ", count_evens([1, 3, 5])


def count9(L):
    counter = 0
    for x in (L):
        if x == 9:
            counter = counter + 1
        else:
            counter = counter + 0
    return counter
print "count9([1, 2, 9]), 1 == ",count9([1, 2, 9])
print "count9([1, 9, 9]), 2 == ",count9([1, 9, 9])
print "count9([1, 9, 9, 3, 9]), 3 == ",count9([1, 9, 9, 3, 9])


def printRect( width, height, symbol):
    for x in range(height):
        print (symbol*width)
printRect( 4, 6, '%' )


def printTriangle( width, symbol, rightSideUp):
    bringback = 0
    rightSideUpBringBack = width +1
    if rightSideUp == True:
        for x in range(width):
            bringback = bringback + 1
            print (bringback*symbol)
    else:
        for x in range(width):
            rightSideUpBringBack = rightSideUpBringBack - 1
            print (rightSideUpBringBack*symbol)
printTriangle( 3, '@', True)
printTriangle( 3, '@', False )


def printBumps( num, symbol1, symbol2 ):
    for x in range(num+1):
        printTriangle(x,symbol1,True)
        printTriangle(x,symbol2,False)
print printBumps( 4, '%', '#' )


def printDiamond(width, symbol):
    diamondstart = 0
    if x < width: #NOT DONE KEEP WORKING ON THIS ONE!!!!!
        for x in range(width):
            diamondstart = diamondstart + 1
            print diamondstart*symbol
        if x == width:
            print diamond
printDiamond( 3, '&' )

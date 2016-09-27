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
    result = 0
    for e in L:
        result = result + e  # or result += e
    return result
# tests!
print "summed( [4,5,6] ): should be 15 == ", summed( [4,5,6] )
print "summed( range(3,10) ): should be 42 == ", summed( range(3,10) )
#I have made the changes listed in my Problem Set 2 feedback

import math

def tpl(x):
    """
    tpl puts out three times the x value given
    """
    return 3*x
print 'tpl(3) is', tpl(3)

def sq(x):
    """
    sq puts out the number x squared
    """
    return x**2
print 'sp(4) is', sq(4)

def interp(low,high,frac):
    """
    takes y-x and multiplies by z
    """
    return ((high-low)*frac)+low
print 'interp(4,16,.25) is', interp(4,16,.25)

def checkends(wordywordword):
    """
    function compares first and last character to see if they match and outputs true if they do, and false
    if they don't
    """
    if wordywordword[0] == wordywordword[-1]:
        return True
    else:
        return False
print 'checkends(tyler lockett) is', checkends('tyler lockett')
print 'checkends(fun) is', checkends('fun')

def flipside(s):
    """
    flips the input s by putting the first half second, and the second half first
    """
    halflength = len(s)/2
    len(s)%2 == 0
    return s[halflength:] + s[0:halflength]
print flipside('belltoll')
print flipside('carpets')

def convertFromSeconds(s):
    """
    takes in seconds and gives out four new sets of data [days, hours, minutes, seconds]
    """
    d = s/(24*60*60)
    s = s%(24*60*60)
    h = s/(60*60)
    s = s%(60*60)
    m = s/60
    s = s%60
    return [d,h,m,s]
print '123010 seconds is ', convertFromSeconds(123010)

def front3(s):
    """
    Given a string, we'll say that the
    front is the first 3 chars of the string.
    If the string length is less than 3,
    the front is whatever is there. Return a new
    string which is 3 copies of the front.
    """
    return s[0:3] + s[0:3] + s[0:3]
print front3('funny')

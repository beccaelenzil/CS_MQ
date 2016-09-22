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
    if len(s)%2 == 0:
        return s[halflength:] + s[0:halflength]
    elif len(s)%2 == 1:
        return s[(halflength +1):] + s[0:(halflength +1)]
print flipside('belltoll')

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



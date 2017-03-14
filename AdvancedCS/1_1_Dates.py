# python 2
#
# Problem Set 1, Problem 1: Dates
#
# Name:
#

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
        as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def tomorrow(self):
        if self.isLeapYear() == True:
            feb = 29
        else:
            feb = 28

        DIM = [0,31,feb,31,30,31,30,31,31,30,31,30,31]


        if self.day < DIM[self.month]:
            self.day += 1
        elif self.day == DIM[self.month] and self.month != 12:
            self.month += 1
            self.day = 1
        elif self.month == 12 and self.day == DIM[self.month]:
            self.year += 1
            self.month = 1
            self.day =1
        return self


# create an object named d with the constructor
d = Date(11, 12, 2014)  # use day 11 if you prefer

# show d's value
print d


# a printing example
print 'Wednesday is', d


# create another object named d2
# of *the same date*
d2 = Date(11, 12, 2014)

# show its value
print d2


# are they the same?
d == d2


# look at their memory locations
id(d)   # return memory address
#413488      # your result will be different

id(d2)  # again
#430408      # this should differ from above!

# check if dtwo is in a leap year it is!
print d2.isLeapYear()
#False

# yet another object of type Date
# a distant New Year's Day
d3 = Date(1, 1, 2020)

# check if d3 is in a leap year
print d3.isLeapYear()

d = Date(1, 1, 2015)
d2 = d
id(d)
#430542      # your memory address may differ
id(d2)
#430542      # but d2 should be the SAME as d!
d == d2
#True        # so this should be True


d = Date(12, 17, 2015)
d2 = d.copy()
print d
#01/01/2015
print d2
#01/01/2015

id(d)
#430568      # your memory address may differ
id(d2)
#413488      # but d2 should be different from d!
print d == d2

print " "

print d.tomorrow()


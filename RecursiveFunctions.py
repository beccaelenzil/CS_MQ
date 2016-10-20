#https://trinket.io/library/trinkets/b801a2b8d4

def fibIter(n):
    fibSeq = [0,1]
    if n == 1:
        print '0'
        return 0
    elif n == 2:
        print '0'
        print '1'
        return 1
    else:
        print '0'
        print '1'
        for i in range (2,n):
            fibSeq.append(fibSeq[i-1] + fibSeq[i-2])
            print fibSeq[-1]
        return fibSeq[-1]
#fibIter(8)


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#print fib(8)


def listReverseIter(L):
    if len(L) == 0:
        return 'Enter a string of numbers'
    elif len(L) == 1:
        return L
    else:
        return L[::-1]
#print listReverseIter([1,2,3,4,5])


def listReverseIterDifferent(L):
    K = []
    for i in range(len(L)-1, -1, -1):
        K.append(L[i])
    return K
#print listReverseIterDifferent([10,9,8,7])

def listReverse(L):
    if len(L) == 1:
        return L
    elif len(L) == 0:
        return 'error'
    else:
        return [L[-1]] + listReverse(L[0:-1])
print listReverse([42,23,16,15,8,4])



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

fibIter(8)


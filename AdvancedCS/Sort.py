#SORT
# File: Sort.py
# Verions: Python 2.7.13
# Name: Matt Querdasi
# Date: 4/13/17
# Desc: PROG DESC
# Usage: Sort class

import random

def mergeSort(alist):
    print "Splitting ",alist
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print "Merging ",alist

"""
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
"""

def quickSort(some_list, start, stop):
    if stop - start < 1:
        return some_list

    else:
        pivot = some_list[start]

        while start <= stop:
            while some_list[start] < pivot:
                start += 1
            while some_list[stop] > pivot:
                stop -= 1

            if start <= stop:
                some_list[start], some_list[stop] = some_list[stop], some_list[start]
                start += 1
                stop -= 1

        print some_list

        quickSort(some_list, start, stop)
        quickSort(some_list, start, stop)

my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
quickSort(my_list, 0, len(my_list) - 1)

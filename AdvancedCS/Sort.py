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
    print my_list

    if stop - start < 1:
        return some_list

    else:
        pivot = some_list[start]
        left = start
        right = stop

        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1

            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                left += 1
                right -= 1

        print some_list

        quickSort(some_list, start, right)
        quickSort(some_list, left, stop)

        return some_list



my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]

my_list_sorted = quickSort(my_list, 0, len(my_list) - 1)





def my_selection_sort(some_list):
    print some_list

    for i in range(len(some_list)):
        smallest_value = i
        print some_list[smallest_value]

        for j in range(i+1,len(some_list)):
            if some_list[j] < some_list[smallest_value]:
                #store values as new varibles
                new_smallest_value = some_list[j]
                switch_value = some_list[smallest_value]

                #transfer/switch values with new variables
                some_list[j] = switch_value
                some_list[smallest_value] = new_smallest_value

                j += 1
            else:
                j += 1

        print some_list
        i += 1

    return some_list

test_list = [11, 4, 76, 3, 730, 6, 10, 46, 99, 2]
test_list_sorted = my_selection_sort(test_list)


def my_insertion_sort(some_list):
    print some_list
    for i in range(1, len(some_list)):
        while i > 0 and some_list[i] < some_list[i-1]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i-=1
            print some_list
    return some_list


def shellSort(some_list, gap):
    #condenses the numbers closer to where they belong
    for j in range(gap):
        gap_list = []
        for i in range(j, len(some_list), gap):
            gap_list.append(some_list[i])
        print gap_list
        gapList = my_insertion_sort(gap_list)
        print gap_list
        z = 0
        for i in range(j, len(some_list), gap):
            some_list[i] = gapList[z]
            z+=1
        print some_list


    return my_insertion_sort(some_list)

def bubbleSort(some_list):
    switch = True
    while switch == True:
        switch = False

#need to add statement

'''
Derek Yang
CS 325 Spring 2018
Homework 1 - Insertion Sort Extra Credit
Uses nested loops to sort and is very inefficient.

Worst Case:
Inputs are in reverse order.  Ex: 9,8,7,6,5,4,3,2,1 turns into 1,2,3,4,5,6,7,8,9
Best Case:
Inputs are sorted so you only do one comparison.  Ex: 1,2,3,4,5 turns into 1,2,3,4,5
'''

import random
import time

def insertsort(arr):
    # start at one because we assume that the first item is sorted
    for i in range(1,len(arr)):
        # holds the unsorted portion
        tmp = arr[i]
        idx = i
        while idx>0 and tmp<arr[idx-1]:
            # shift items over to make room for curr item
            arr[idx] = arr[idx-1]
            idx += -1
        arr[idx] = tmp
    return arr


arr_combined = []

# returns a list in sorted order
def best_arr(n):
    tmp = list(range(n))
    print(tmp)
    return tmp


# returns list in reversed order
def worst_arr(n):
    tmp = list(reversed(range(n)))
    return tmp

# tracks time
def count_runs(arr):
    time_start = time.time()
    arr = insertsort(arr)
    print("Count: "+str(time.time()-time_start))

# print the best case
n_1000 = best_arr(1000)
n_2000 = best_arr(2000)
n_5000 = best_arr(5000)
n_10000 = best_arr(10000)

print("Best count for n = 1000")
count_runs(n_1000)
print("Best count for n = 2000")
count_runs(n_2000)
print("Best count for n = 5000")
count_runs(n_5000)
print("Best count for n = 10000")
count_runs(n_10000)

# print the worst case
n_1000 = worst_arr(1000)
n_2000 = worst_arr(2000)
n_5000 = worst_arr(5000)
n_10000 = worst_arr(10000)

print("Worst count for n = 1000")
count_runs(n_1000)
print("Worst count for n = 2000")
count_runs(n_2000)
print("Worst count for n = 5000")
count_runs(n_5000)
print("Worst count for n = 10000")
count_runs(n_10000)


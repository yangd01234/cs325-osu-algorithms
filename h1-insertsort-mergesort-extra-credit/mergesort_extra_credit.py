import random
import time
'''
Derek Yang
CS 325 Spring 2018
Homework 1 - Merge Sort Extra Credit

Partitions the list in half and sort each side.
The leftmost item is the smallest item in each list.

To generate the worst case:
You have to get the max number of comparisons where every item will be compared at least once
split the array into odds and evens.  ex: [0,2,4,1,3,5]

To generate the best case:
The array is already in sorted order so you don't have to compare.
ex: [0,1,2,3,4,5]
'''




# recursive function to mergesort
def mergesort(arr):

    if len(arr) <=1:
        return arr
    middle = int(len(arr)/2)
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    # merge both
    return merge(left,right)

# merge helper function
def merge(left,right):
    tmp = []
    i = j = 0
    if left[i]<right[j]:
        while i<len(left) and j<len(right):
            # compare the elements at the top of each arr
            if left[i]<right[j]:
                tmp.append(left[i])
                i+=1
            else:
                tmp.append(right[j])
                j+=1
    tmp += left[i:]
    tmp += right[j:]
    return tmp

arr_combined = []

# returns a list in sorted order
def best_arr(n):
    tmp = list(range(n))
    print(tmp)
    return tmp


# returns list in split order.  Use list comprehension!
def worst_arr(n):
    even = [x for x in range(n) if x %2 == 0]
    odd = [i for i in range(n) if i % 2 !=0]
    return odd+even

# tracks time
def count_runs(arr):
    time_start = time.time()
    arr = mergesort(arr)
    print("Count: "+str(time.time()-time_start))

#print the best case
n_1000 = best_arr(1000)
n_2000 = best_arr(2000)
n_5000 = best_arr(5000)
n_10000 = best_arr(10000)
n_20000 = best_arr(20000)

print("Best count for n = 1000")
count_runs(n_1000)
print("Best count for n = 2000")
count_runs(n_2000)
print("Best count for n = 5000")
count_runs(n_5000)
print("Best count for n = 10000")
count_runs(n_10000)
print("Best count for n = 20000")
count_runs(n_20000)

#print the worst case
n_1000 = worst_arr(1000)
n_2000 = worst_arr(2000)
n_5000 = worst_arr(5000)
n_10000 = worst_arr(10000)
n_20000 = worst_arr(20000)

print("Worst count for n = 1000")
count_runs(n_1000)
print("Worst count for n = 2000")
count_runs(n_2000)
print("Worst count for n = 5000")
count_runs(n_5000)
print("Worst count for n = 10000")
count_runs(n_10000)
print("Worst count for n = 20000")
count_runs(n_20000)


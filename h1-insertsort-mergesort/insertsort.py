'''
Derek Yang
CS 325 Spring 2018
Homework 1 - Insertion Sort
Uses nested loops to sort and is very inefficient.
'''

def insertsort(arr):
    # we start at one because we assume that the first item is sorted
    for i in range(1,len(arr)):
        # holds the unsorted portion
        tmp = arr[i]
        idx = i
        while idx > 0 and tmp < arr[idx-1]:
            # shift items over to make room for curr item
            arr[idx] = arr[idx-1]
            idx += -1
        arr[idx] = tmp
    return arr

# open the data file and create a list of lists
arr_combined = []

# open and read data.txt
f = open("data.txt",'r+')

for x in f:
    test = [int(i) for i in x.split()]
    test.pop(0)
    arr_combined.append(test)


# iterate through the list and sort
for x in range(0,len(arr_combined)):
    print(arr_combined[x])#print the original
    arr_combined[x] = insertsort(arr_combined[x])

# print list
for x in arr_combined:
    print(x)

# write to insert.out
f_two = open("insert.out","w+")
for x in arr_combined:
    for y in x:
        f_two.write("%d "%y)
    f_two.write("\n")

f_two.close()
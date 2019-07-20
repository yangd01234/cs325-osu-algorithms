'''
Derek Yang
CS 325 Spring 2018
Homework 1 - Merge Sort
Partitions the list in half and sort each side.
The leftmost item is the smallest item in each list.
'''

# recursive function to mergesort
def mergesort(arr):

    # checks length of array
    if len(arr) <=1:
        return arr
    
    # partitions array into two parts
    middle = int(len(arr)/2)
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    #merge both
    return merge(left,right)

# merge helper function
def merge(left,right):
    tmp = []
    i = j = 0
    while i<len(left) and j<len(right):
        # compare the elements at the top of each arr
        if left[i]<right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1
    # push the last element of each onto the array
    if i == len(left):
        tmp.extend(right[j:])
    else:
        tmp.extend(left[i:])
    return tmp


# open and read the data file
arr_combined = []

f = open("data.txt",'r+')

for x in f:
    test = [int(i) for i in x.split()]
    test.pop(0)
    arr_combined.append(test)


# iterate through the list
for x in range(0,len(arr_combined)):
    arr_combined[x] = mergesort(arr_combined[x])

# write to merge.out
f_two = open("merge.out","w+")
for x in arr_combined:
    for y in x:
        f_two.write("%d "%y)
    f_two.write("\n")

f_two.close()



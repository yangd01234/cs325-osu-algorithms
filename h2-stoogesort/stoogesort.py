import math

'''
Derek Yang
CS 325 Spring 2018
Homework 2 - Stooge Sort

Recusivley sort an array using stoogesort.  Within stoogesort,
the array will be split into 2/3 where the first portion will be sorted,
then the end, and then the start again. The three stooges!
'''

# recursive stoogesort
def stoogesort(arr, start, end):
    # base case
    if start >= end:
        return
    
    if arr[start]>arr[end]:
        arr[end],arr[start] = arr[start], arr[end]
    
    # split the list into three parts
    if end-start+1 > 2:
        middle = math.ceil((end-start)/3)
        stoogesort(arr,start,end-middle)
        stoogesort(arr,start+middle,end)
        stoogesort(arr, start, end - middle)

# read data.txt
arr_combined = []

f = open("data.txt",'r+')

for x in f:
    test = [int(i) for i in x.split()]
    test.pop(0)
    arr_combined.append(test)
f.close()

# iterate through the list
for x in range(0,len(arr_combined)):
    print("Original: "+str(arr_combined[x]))
    stoogesort(arr_combined[x],0,len(arr_combined[x])-1)

# print sorted list
for x in arr_combined:
    print("Sorted: "+str(x))

# write ordered list to stooge.out
f_two = open("stooge.out","w+")
for x in arr_combined:
    for y in x:
        f_two.write("%d "%y)
    f_two.write("\n")

f_two.close()
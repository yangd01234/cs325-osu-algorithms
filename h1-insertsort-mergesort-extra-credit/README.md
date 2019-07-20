# Homework 1 Extra Credit - Insert Sort and Merge Sort Worst and Best Cases
Derek Yang
CS 325 - Algorithms
Spring 2018

## Required Files:
insertionsort_extra_credit.py and mergesort_extra_credit.py

## Output: 
Prints results to terminal

## Summary:
Insertion Sort Question 5 Extra Credit
Uses nested loops to sort and is very inefficient.

Worst Case:
Inputs are in reverse order.  Ex: 9,8,7,6,5,4,3,2,1 turns into 1,2,3,4,5,6,7,8,9
Best Case:
Inputs are sorted so you only do one comparison.  Ex: 1,2,3,4,5 turns into 1,2,3,4,5


Merge Sort Extra Credit
Partitions the list in half and sort each side.
The leftmost item is the smallest item in each list.

To generate the worst case:
You have to get the max number of comparisons where every item will be compared at least once
split the array into odds and evens.  ex: [0,2,4,1,3,5]

To generate the best case:
The array is already in sorted order so you don't have to compare.
ex: [0,1,2,3,4,5]

## How to run:
``` bash
$ python3 insertionsort_extra_credit.py
$ python3 mergesort_extra_credit.py
```


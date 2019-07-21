# osu-algorithms
Collection of work from Spring 2018 Algorithms (CS 325) course at Oregon State University.

# Table of Contents
## Homework 1 - InsertSort and MergeSort
Summary:
These programs will read and sort the data.txt file and then output as either insert.out or merge.out. The first value of each line within data.txt is the number of integers that need to be sorted, followed by the integers.

## Homework 1 Extra Credit - Insert Sort and Merge Sort Worst and Best Cases
Summary:
Insertion Sort Question 5 Extra Credit Uses nested loops to sort and is very inefficient.

Worst Case: Inputs are in reverse order. Ex: 9,8,7,6,5,4,3,2,1 turns into 1,2,3,4,5,6,7,8,9 Best Case: Inputs are sorted so you only do one comparison. Ex: 1,2,3,4,5 turns into 1,2,3,4,5

Merge Sort Extra Credit Partitions the list in half and sort each side. The leftmost item is the smallest item in each list.

To generate the worst case: You have to get the max number of comparisons where every item will be compared at least once split the array into odds and evens. ex: [0,2,4,1,3,5]

To generate the best case: The array is already in sorted order so you don't have to compare. ex: [0,1,2,3,4,5]

## Homework 2 - Stooge Sort
Summary:
This program will sort an array/list using the stoogesort method. The stoogesort method divides the array into 2/3. First recursivley sorting the first fraction, the second fraction, and then the first fraction again. Written in Python 3

## Homework 3 - Dynamic Programming Change Problem
Summary:
This program will use the functions get_min_coins and count_coins to get the minimum number of coins needed for a total and it's denominations of each coin.

## Homework 4 - Greedy Algorithms Scheduler
Summary:
In this program, we take a file named "act.txt" and process the activities inside. Each will be processed using the last to start method. The sort is used with python's build in sort function. 

## Homework 5 - Breadth First Search Wrestlers
Summary:
This program will implement breadth first search using the input from a text file. The user will input a text file name at runtime and the program will go through and use breadth first search to categorize each wrestler as a "baby face" or "heel". Each wrestler is given a pre-determined rivalry from the text file. The program will use BFS to check if this is possible or not. All results will be outputted into the terminal.

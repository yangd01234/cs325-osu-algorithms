'''
Derek Yang
CS 325 Spring 2018
Homework 2 - Minimal Change program
This program will use the functions get_min_coins and count_coins
to get the minimum number of coins needed for a total and it's
denominations of each coin.
'''

import sys
import time

def get_min_coins(coins, target_amount,coin_a):
    # list to track values
    table = [0]*(target_amount+1)
    for i in range(target_amount+1):
        # number of coins
        num_coins = i
        # coin type/value
        tmp_coin = 1
        for j in coins:
            # make sure that j < current amt, include a case if denom is 0
            if j <= i and j>0:
                # if current pos in table is less than current target amt
                if table[i-j] +1<num_coins:
                    # set the current target current pos
                    num_coins = table[i-j]+1
                     # since it fits, set current coin type/value
                    tmp_coin = j
            table[i] = num_coins
            coin_a[i] = tmp_coin
    return table[target_amount]

# count number of coins
def count_coins(coins,target_amount,coins_a):
    tmp = [0]*(len(coins)) #create a temporary array
    tmp_target = target_amount
    while tmp_target>0 :#first loop through coins
        pos = coins.index(coins_a[tmp_target])
        tmp[pos] = tmp[pos]+1
        tmp_target = tmp_target-coins_a[tmp_target]
    return tmp


# read the data file amount.txt
arr_denomination = []
arr_total = []

f = open("amount.txt",'r+')

counter = 1

for x in f:
    list_tmp = [int(i) for i in x.split()]
    if counter % 2 == 0:
        # total amounts
        arr_total.append(int(x))
    else:
        # denominations
        arr_denomination.append(list_tmp)
    counter += 1
f.close()

'''
Find minimums in the following order:
--denominations
--total amt
--minimum number of each denominations
--minimum number of coins needed
'''
change_txt = open("change.txt","w+")

for x in range(len(arr_total)):
    print("Value "+str(x+1))
    c = [0]*(arr_total[x]+1)
    # coin denominations
    print(arr_denomination[x])
    change_txt.write("%s\n" % str(arr_denomination[x]).replace('[','').replace(']','').replace(',',''))
    # coin total
    print(arr_total[x])
    change_txt.write("%d\n" % arr_total[x])
    min_total = get_min_coins(arr_denomination[x],arr_total[x],c)
    coin_counts = count_coins(arr_denomination[x], arr_total[x], c)
    # min denominations
    print(coin_counts)
    change_txt.write("%s\n" % str(coin_counts).replace('[','').replace(']','').replace(',',''))
    # min coins needed
    print(min_total)
    change_txt.write("%d\n" % min_total)

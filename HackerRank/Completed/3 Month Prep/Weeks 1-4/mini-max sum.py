
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.9.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      Time Conversion

#~ -----------------------------------------------------------------


#^ Description
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.







#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    lowest = arr[0]
    highest = arr[0]
    min = None
    max = None
    subtotal = 0
    
    for ele in arr:
        if ele > highest:
            highest = ele
        elif ele < lowest:
            lowest = ele
        
        subtotal += ele
    
    min = subtotal - highest
    max = subtotal - lowest
    
    print(str(min) + ' ' + str(max))

if __name__ == '__main__':

    arr = [1,2,3,4,5]
    # arr = [2,1,3,4,5]
    # arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
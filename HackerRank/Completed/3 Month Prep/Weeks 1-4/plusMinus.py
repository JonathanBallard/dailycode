
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.9.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      Time Conversion

#~ -----------------------------------------------------------------

#^ Description
# Receive Array (int arr[n]: an array of integers) of positive numbers, negative numbers, and zero. 
# Print ratios of positives/negatives/zeros ( positives / number of elements )
# Print the decimal value of each fraction on a new line with  places after the decimal.





#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    numZero = 0
    numPos = 0
    numNeg = 0
    numEle = len(arr)
    
    for ele in arr:
        if ele == 0:
            numZero += 1
        if ele > 0:
            numPos += 1
        if ele < 0:
            numNeg += 1
    
    print("{:.6f}".format(numPos/numEle))
    print("{:.6f}".format(numNeg/numEle))
    print("{:.6f}".format(numZero/numEle))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)





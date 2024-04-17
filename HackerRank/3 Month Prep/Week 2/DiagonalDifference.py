
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.14.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Diagonal Difference

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    length = len(arr)
    midway = math.floor(len(arr) / 2)
    
    diag1 = arr[0][0] + arr[length - 1][length - 1]
    diag2 = arr[0][length - 1] + arr[length - 1][0]
    i = 1
    
    while i < (length - 1):
        diag1 += arr[i][i]
        diag2 += arr[i][length - 1 - i]
        
        i += 1
    
    if(diag1 < 0):
        diag1 *= -1
    if(diag2 < 0):
        diag2 *= -1
        
    if(diag1 >= diag2):
        res = diag1 - diag2
    else:
        res = diag2 - diag1
        
    return res

if __name__ == '__main__':

    arr = [[1,2,3],[4,5,6],[7,8,9]]
    arr2 = [[4,8,3],[7,5,6],[1,2,9]]
    arr3 = [[11,2,4],[4,5,6],[10,8,-12]]
    arr4 = [[-1,1,-7,-8],[-10,-8,-5,-2],[0,9,7,-1],[4,4,-2,1]]

    result = diagonalDifference(arr4)
    
    print(result)



















#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         5.1.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Closest Numbers

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    
    arr.sort()
    retArr = []
    i = 0
    currMin = 10000
    diff = 0
    
    while i < len(arr) - 1:
        diff = arr[i + 1] - arr[i]
        if(diff < currMin):
            currMin = diff
            retArr = []
            retArr.append(arr[i])
            retArr.append(arr[i + 1])
        elif(diff == currMin):
            retArr.append(arr[i])
            retArr.append(arr[i + 1])
        
        i += 1
    
    return retArr




if __name__ == '__main__':

    arr = [5,2,3,4,1]

    result = closestNumbers(arr)

    print(result)















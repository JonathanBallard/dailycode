
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         5.2.28
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Minimum Absolute Difference in an Array

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    
    arr.sort()
    
    abs = 0
    min = arr[len(arr) - 1]
    i = 0
    
    
    while i < len(arr) - 1:
        
        abs = arr[i] - arr[i + 1]
        
        if abs < 0:
            abs *= - 1
            
        if abs < min:
            min = abs
            
        if min == 0:
            return 0
        
        i += 1
    
    return min

if __name__ == '__main__':

    arr = [-2,2,4]
    arr = [3,-7,0]
    arr = [-59,-36,-13,1,-53,-92,-2,-96,-54,75]

    result = minimumAbsoluteDifference(arr)
    print(result)















#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.18.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      Sub-Array Division 2

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    
    n = len(s)
    arr = [0] * m
    i = 0
    sum = 0
    numWays = 0
    
    
    while i < n - m + 1:
        j = 0
        sum = 0
        arr = [0] * m
        
        while j < m:
            sum += s[i + j]
            arr[j] += s[i + j]
            j += 1
            
        if(sum == d):
            numWays += 1
        # print(str(arr) + ' = ' + str(sum))
        
        i += 1
    
    return numWays
    

if __name__ == '__main__':

    s = [2,2,1,3,2,2,4,1,2,1,1,2,1,4,2,2]
    
    first_multiple_input = [7,3]

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)















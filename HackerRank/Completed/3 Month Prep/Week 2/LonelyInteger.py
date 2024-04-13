
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.13.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Lonely Integer

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(arr):
    # Write your code here
    
    arr.sort()
    i = 0
    
    while(i < len(arr)):
        if(i == len(arr) - 1):
            return arr[i]
        elif(arr[i] == arr[i + 1]):
            i += 2
        else:
            return arr[i]


if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # a = list(map(int, input().rstrip().split()))

    a3 = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
    a2 = [41,20,13,40,13,20,41,96,96]
    a = [1,2,3,4,3,2,1]
    n = len(a)
    
    result = lonelyinteger(a)
    
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()



















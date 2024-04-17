
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.12.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      Week 1 Mock Test - Find the Median

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

import math

def findMedian(arr):
    # Write your code here

    arr.sort()
    length = len(arr)

    idx = math.floor(length / 2)
    median = arr[idx]
    
    return median
    
    
    
    
    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    
    arr = [3,2,8,5,1,4,9,6,7]

    result = findMedian(arr)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()



















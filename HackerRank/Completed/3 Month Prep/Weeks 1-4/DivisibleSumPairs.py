
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.9.24
# Site:         HackerRank
# Section:      3 Month Prep - Week x
# Problem:      xxx

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    arr = sorted(ar)
    
    i = 0
    j = 1
    numPairs = 0
    
    while(i < n - 1):
        j = i + 1
        
        while(j < n):
            if((arr[i] + arr[j]) % k == 0):
                numPairs += 1
            j += 1
        
        i += 1
    
    return numPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


















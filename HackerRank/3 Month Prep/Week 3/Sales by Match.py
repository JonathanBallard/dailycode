
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.17.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      Sales By Match

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    ar.sort()
    retD = {}
    numPairs = 0
    i = 0
    
    while i < len(ar):
        if not (ar[i] in retD):
            retD[(ar[i])] = 1
        else:
            retD[(ar[i])] += 1
        
        i += 1
    
    for val in retD.values():
        numPairs += math.floor(val / 2)
    
    return numPairs


if __name__ == '__main__':

    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(result)















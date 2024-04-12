
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.9.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      Breaking The Records

#~ -----------------------------------------------------------------




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    lowest = scores[0]
    highest = scores[0]
    lowRec = 0
    highRec = 0
    
    for score in scores:
        if score < lowest:
            lowest = score
            lowRec += 1
        elif score > highest:
            highest = score
            highRec += 1
    return [highRec, lowRec]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
















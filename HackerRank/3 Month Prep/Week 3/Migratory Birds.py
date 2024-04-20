
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.20.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      Migratory Birds

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    arr.sort()
    
    i = 1
    currBird = highBird = arr[0]
    currCount = highCount = 1
    
    while i < len(arr):
        if arr[i] == currBird:
            currCount += 1
            if currCount > highCount:
                highCount = currCount
                highBird = currBird
        else:
            currBird = arr[i]
            currCount = 1
        i += 1
    
    return highBird

if __name__ == '__main__':

    arr = [1,3,1,2,2,3,3,2,3]

    result = migratoryBirds(arr)
    print(result)















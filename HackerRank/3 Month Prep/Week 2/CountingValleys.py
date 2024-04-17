
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.15.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Counting Valleys

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    
    altitude = 0
    valleys = 0
    i = 0
    
    while i < steps:
        if (path[i] == 'D'):
            if (altitude == 0):
                valleys += 1
            altitude -= 1
        elif (path[i] == 'U'):
            altitude += 1
        i += 1
    
    return valleys

if __name__ == '__main__':


    path = 'UDDDUDUU'
    steps = len(path)

    result = countingValleys(steps, path)

    print(result)



















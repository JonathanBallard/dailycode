
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.16.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Mars Exploration

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    
    i = 0
    errors = 0
    
    while i < len(s):
        if not (s[i] == 'S'):
            errors += 1
        if not (s[i + 1] == 'O'):
            errors += 1
        if not (s[i + 2] == 'S'):
            errors += 1
        
        i += 3
    
    return errors


if __name__ == '__main__':

    s = 'SOSSOSSOSSOS'
    s1 = 'SOSSPSSQSSOR'
    s2 = 'SOSSOT'
    s3 = 'SOSSOS'

    result = marsExploration(s)
    print(result)





















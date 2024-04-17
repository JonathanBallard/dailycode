
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.9.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      Time Conversion

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s = time.strptime(s, '%I:%M:%S%p')
    
    hr = s.tm_hour
    min = s.tm_min
    sec = s.tm_sec
    
    if hr < 10:
        hr = '0' + str(hr)
    if min < 10:
        min = '0' + str(min)
    if sec < 10:
        sec = '0' + str(sec)
    
    milTime = str(hr) + ':' + str(min) + ':' + str(sec)
    return milTime

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    
    s = '12:05:45AM'

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()

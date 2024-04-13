
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.12.24
# Site:         HackerRank
# Section:      Project Euler
# Problem:      Multiples of 3 and 5

#~ -----------------------------------------------------------------

#^ --------------------------------------------------------------
#^ UNFINISHED (Failed 2 out of 5 test cases due to runtime error)
#^ --------------------------------------------------------------


#!/bin/python3

import sys


# t = int(input().strip())
input = [15,67, 12,30, 56,12, 1,299]
prevRes = 0
prevNum = 0
maxRes = 0
maxNum = 0

# for a0 in range(t):
for a0 in input:
    arr = []
    sum = 0
    i = 2
    # n = int(input().strip())
    n = a0
    
    if(maxNum < n) and (maxNum > 0):
        sum += maxRes
        i = maxNum
    elif(prevNum < n) and (prevNum > 0):
        sum += prevRes
        i = prevNum

    while (i < n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
        i += 1
    
    if(n > maxNum):
        maxNum = n
        maxRes = sum

    prevRes = sum
    prevNum = n
    print(sum)



















#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.26.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Separate the Numbers

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    
    i = 0
    lastVal = 0
    currVal = 0
    digits =  1
    startVal = 0
    failed = False
    
    while i < len(s):
        
        if(i < len(s) - 1):
            # check if single digit
            if(i == 0):
                a1 =  int(str(s[i + 1] + str(s[i + 2])))
                a2 = int(str(s[i + 2]) + str(s[i + 3]))
                a3 = int(str(s[i]) + str(s[i + 1]))
                
                # 1 digit
                if(int(s[i + 1]) - int(s[i]) == 1):
                    print((s[i + 1]) + (s[i]))
                    print('single digit startVal: ' + str(s[i]))
                    startVal = s[i]
                    currVal = s[i]
                    
                # 1 to 2 digits
                elif(int(s[i]) == 9):
                    
                    if(int(a1) - 9 == 1):
                        digits = 2
                        currVal = 9
                        startVal = 9
                # 2 digits
                elif(a2 - a3 == 1):
                    digits = 2
                    currVal = a3
                    startVal = a3
                
            else:
                # if a multi-digit sequence that doesn't start at '0'
                if(i < len(s) - 3):
                    a1 = int(str(s[i]) + str(s[i + 1]))
                    a2 = int(str(s[i + 2]) + str(s[i + 3]))
                    if(int(s[i + 2]) == int(s[i]) and int(s[i + 3]) == int(s[i + 1]) + 1):
                        currVal = int(str(s[i]) + str(s[i + 1]))
                        digits = 2
                    elif(a2 - a1 == 1):
                        digits = 2
                        currVal = a1
                
                # look for 2 digits
                if(s[i + 1] == 0):
                    currVal = int(str(s[i]) + '0')
                    digits = 2
                    print('currVal: ' + str(currVal))
                elif(digits == 2):
                    currVal = int(str(s[i]) + str(s[i + 1]))
        
        if(digits == 1):
            if(i == s[len(s) - 1]):
                currVal = s[len(s) - 1]
        
        if(lastVal == 0):
            startVal = currVal
        elif(lastVal > 0):
            if not (currVal - lastVal == 1):
                failed = True
                print('NO')
                return 'NO'
                
        
        lastVal = int(currVal)
        i += digits
    
    if(failed == True):
        print('NO')
        return 'NO'
    else:
        print('YES ' + str(startVal))
        return 'YES ' + str(startVal)
    


if __name__ == '__main__':

    s = '10111213'
    s2 = '010203'
    s3 = '1920212223'

    separateNumbers(s3)
















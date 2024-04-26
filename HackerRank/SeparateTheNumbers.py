
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
    
    s = str(s)
    i = 1
    subArr = [s[0]]
    pNum = 0
    iNum = 0
    nNum = 0
    
    
    if(s[0] == '0'):
        return 'NO'
    
    while i < len(s):
        ax = 0
        compPrev = int(s[i - 1])
        compI = int(s[i])
        
        if(int(s[i]) == 9):
            if(i + 2 < len(s) and int(s[i + 2]) == 0):
                nNum = int(''.join(s[i + 1]).join('0') )
        
        # if '0'
        if(i < len(s) - 1):
            compNext = int(s[i + 1])
            if(compI == 0 and compNext == 0):
                compPrev = int(''.join(compPrev).join('00'))
                pNum = compPrev
                ax = 2
            elif(compI == 0):
                compPrev = int(str(compPrev) + '0')
                pNum = compPrev
                ax = 1
            elif(int(compNext) == 0):
                compI = int(str(compI) + '0')
                iNum = compI
                ax = 1
        elif(compI == 0):
            compPrev = int(str(compPrev) + '0')
            ax = 1
        
        if(compI - compPrev == 1):
            subArr.append(s[i])
        else:
            if(len(subArr) > 1):
                print('YES ' + str(subArr[0]))
                return
            else:
                print('NO')
                return
        
        
        i += 1 + ax
    
    print('YES ' + str(subArr[0]))
    return


if __name__ == '__main__':

    s = 10111213

    separateNumbers(s)
















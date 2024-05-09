
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.30.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Caesar Cipher

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    
    k %= 26
    
    alph = 'abcdefghijklmnopqrstuvwxyz'
    alphU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decoded = alph[k:] + alph[: k]
    decodedU = alphU[k:] + alphU[: k]
    retStr = ''
    char = ''
    chrIndex = 0
    i = 0
    
    while i < len(s):
        char = s[i]
        chrIndex = alph.find(char)
        if chrIndex >= 0:
            retStr += decoded[chrIndex]
        else:
            chrIndex = alphU.find(char)
            if chrIndex >= 0:
                retStr += decodedU[chrIndex]
            else:
                retStr += char
        i += 1
    
    return retStr

if __name__ == '__main__':


    s = "middle-Outz"
    s = "www.abc.xy"

    k = 87

    result = caesarCipher(s, k)

    print(result)
















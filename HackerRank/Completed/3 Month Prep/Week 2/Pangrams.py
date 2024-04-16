
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.16.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Pangrams

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    
    d = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    
    s = s.lower()
    
    for chr in s:
        if((not chr == ' ') and (d[chr] == 0)):
            d[chr] += 1
    
    if(sum(d.values()) < 26):
        return 'not pangram'
    else:
        return 'pangram'


if __name__ == '__main__':
    s = 'We promptly judged antique ivory buckles for the next prize'
    s1 = 'We promptly judged antique ivory buckles for the prize'
    
    
    result = pangrams(s1)
    
    print(result)
























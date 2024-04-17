
#~ --------------------------------=--------------------------------

#*                           *** SANDBOX ***
#*                           Jonathan Ballard

#~ --------------------------------=--------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys


def sandbox(p1, p2, arr):
    
    arr = arr or [3,3,3]
    length = len(arr)
    
    i = 0
    result = 0
    
    while i < length:
        result += arr[i]
        i += 1
    
    return result

if __name__ == '__main__':

    a1 = 1
    a2 = 2
    array = [1,2,3]

    result = sandbox(a1, a2, array)

    print(result)
























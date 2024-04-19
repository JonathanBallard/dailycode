
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.18.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      XOR Strings 3

#~ -----------------------------------------------------------------

# debug existing function


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = '10101'
t = '00101'
print(strings_xor(s, t))



















#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.21.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      Zig-Zag Sequence (Debug)

#~ -----------------------------------------------------------------

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

a = [2,3,5,1,4,7,6]
n = len(a)
findZigZagSequence(a, n)


#  a = [2,3,5,1,4]
# [1,2,3,4,5]
# [1,2,5,4,3]
# [1,2,5,3,4]
# [1,2,5,4,3]
















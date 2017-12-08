from random import choices
import gmpy2
import itertools

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def donum(tc):
    tc = map(str, tc)
    return int("1{}2{}3{}4{}5{}6{}7{}8{}9{}0".format(*tc))

def test():

    for tc in itertools.product(range(0,10), repeat=9):
        thenum = donum(tc)
        sq = gmpy2.isqrt(thenum)
        #print(sq, thenum)
        if sq*sq == thenum:
            break
    print(sq)

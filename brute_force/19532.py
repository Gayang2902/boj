'''[수학은 비대면강의입니다]

'''

import sys

def solution():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
                return (x, y)
            
r = solution()
print(r[0], r[1])
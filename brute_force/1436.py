'''[영화감독 숌]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 10000, 'N Out of range'
    n = 0
    c = 0
    while c < N:
        n += 1
        if '666' in str(n):
            c += 1 
    return n

print(solution())
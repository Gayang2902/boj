'''[설탕 배달]

'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 3 <= N <= 5000, 'N is out of range'

    mins = list()
    for f in range(N // 5, -1, -1):
        remain = N - (f * 5)
        if remain % 3 == 0:
            t = remain // 3
            mins.append(f + t)
    
    return min(mins) if mins else -1

print(solution())
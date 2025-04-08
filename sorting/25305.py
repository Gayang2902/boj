'''[커트라인]
'''

import sys

def solution():
    N, k = map(int, sys.stdin.readline().split())
    assert 1 <= N <= 1000 and 1 <= k <= N, 'Out of range'

    l = list(map(int, sys.stdin.readline().split()))
    l.sort(reverse=True)

    return l[k - 1]

print(solution())
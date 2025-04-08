'''[좌표 정렬하기]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 100000, 'Out of range'

    dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dots.sort()
    for i in range(N):
        print(dots[i][0], dots[i][1])

solution()
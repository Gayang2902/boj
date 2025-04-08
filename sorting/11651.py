'''[좌표 정렬하기 2]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 100000, 'Out of range'

    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dots.sort(key=lambda x: (x[1], x[0]))
    sys.stdout.write('\n'.join(f'{x} {y}' for x, y in dots) + '\n')

solution()
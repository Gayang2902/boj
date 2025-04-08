'''[좌표 압축]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 1000000, 'Out of range'

    coordinate = list(map(int, sys.stdin.readline().split()))
    dicts = {v:k for k, v in enumerate(sorted(set(coordinate)))}

    sys.stdout.write(' '.join(str(dicts[i]) for i in coordinate) + '\n')

solution()
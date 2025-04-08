'''[단어 정렬]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 20000, 'Out of range'
    vocas = sorted(set(sys.stdin.readline().strip() for _ in range(N)), key=lambda x: (len(x), x))

    sys.stdout.write('\n'.join(s for s in vocas) + '\n')

solution()
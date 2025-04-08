'''[숫자 카드]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 500000, 'Out of range'
    cards = list(map(int, sys.stdin.readline().split()))
    
    M = int(sys.stdin.readline())
    assert 1 <= M <= 500000
    numbers = list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        if numbers[i] in cards:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print('')

solution()
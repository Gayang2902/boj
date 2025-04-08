'''[체스판 다시 칠하기]

'''

import sys

W = [
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
]
B = [
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
]

def solution():
    N, M = map(int, sys.stdin.readline().split())
    assert 8 <= N <= 50 and 8 <= M <= 50, 'Out of Range'

    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    mins = list()

    for i in range(N - 7):
        for j in range(M - 7):
            l = sum([board[k][j:j+8] for k in range(i, i + 8)], [])
            # t = W if l[0] == 'W' else B
            m = 0
            for k in range(64):
                if l[k] != W[k]:
                    m += 1
            mins.append(m)
            m = 0
            for k in range(64):
                if l[k] != B[k]:
                    m += 1
            mins.append(m)
    
    return min(mins)
            
print(solution())
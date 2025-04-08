''' [스티커]
'''

import sys

def solution(T: int) -> int:
    for t in range(T):
        N = int(sys.stdin.readline())
        assert 1 <= N <= 100000, 'Out of range'
        tc = [list(map(int, sys.stdin.readline().split())) for i in range(2)]
        ms = list()
        while sum(tc[0] + tc[1]) != N * -2:
            flat = sum(tc, [])
            m = flat.index(max(flat))
            ms.append(flat[m])

            row = m // N
            col = m % N
            tc[row][col] = -1
            if row - 1 >= 0 and tc[row - 1][col] != -1:
                tc[row - 1][col] = -1
            if row + 1 < 2 and tc[row + 1][col] != -1:
                tc[row + 1][col] = -1
            if col + 1 < N and tc[row][col + 1] != -1: 
                tc[row][col + 1] = -1
            if col - 1 >= 0 and tc[row][col - 1] != -1:
                tc[row][col - 1] = -1
        print(sum(ms))

def dp(T: int) -> int:
    for _ in range(T):
        N = int(sys.stdin.readline())
        assert 1 <= N <= 100000, 'Out of range'

        tc = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

        # special case: N이 1인 경우
        if N == 1:
            print(max(tc[0][0], tc[1][0]))
            continue
        
        cache = [[0] * N for _ in range(2)]
        # 시작 지점을 첫 번째 열로 설정
        cache[0][0] = tc[0][0]
        cache[1][0] = tc[1][0]

        cache[0][1] = tc[1][0] + tc[0][1]
        cache[1][1] = tc[0][0] + tc[1][1]
        for i in range(2, N):
            cache[0][i] = max(cache[1][i - 1], cache[1][i - 2]) + tc[0][i]
            cache[1][i] = max(cache[0][i - 1], cache[0][i - 2]) + tc[1][i]

        print(max(cache[0][N - 1], cache[1][N - 1]))
        

T = int(sys.stdin.readline())
dp(T)
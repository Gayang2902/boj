''' [유기농 배추]
인접한 지형을 구하는 문제 -> DFS로 풀이
'''

import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')
sys.setrecursionlimit(10 ** 6)

# 상하좌우 이동
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
def dfs(am, y, x, am_size):
    am[y][x] = 0
    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]
        if 0 <= ny < am_size[0] and 0 <= nx < am_size[1]:
            if am[ny][nx]:
                dfs(am, ny, nx, am_size)

T = int(input())
for _ in range(T):
    # M: 가로, N: 세로, K: 배추의 위치
    M, N, K = map(int, input().split())
    am = [[0] * M for row in range(N)]
    for __ in range(K):
        x, y = map(int, input().split())
        am[y][x] = 1

    cnt = 0
    for row in range(N):
        for col in range(M):
            if am[row][col]:
                dfs(am, row, col, (N, M))
                cnt += 1
    print(str(cnt))
    
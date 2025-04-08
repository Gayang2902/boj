''' [적록색약]
'''

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
normal = []
nonmal = []

for r in range(N):
    norrow = list(input().strip())
    nonrow = norrow[:]
    for i in range(N):
        if nonrow[i] == 'G':
            nonrow[i] = 'R'
    normal.append(norrow)
    nonmal.append(nonrow)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
normal_visited = [[False] * N for _ in range(N)]
nonmal_visited = [[False] * N for _ in range(N)]

def dfs(y, x, m, visited, color):
    visited[y][x] = True

    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]

        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if m[ny][nx] == color and not visited[ny][nx]:
            dfs(ny, nx, m, visited, color)

norrst = 0
nonrst = 0
for i in range(N):
    for j in range(N):
        if normal_visited[i][j] == False:
            dfs(i, j, normal, normal_visited, normal[i][j])
            norrst += 1
        if nonmal_visited[i][j] == False:
            dfs(i, j, nonmal, nonmal_visited, nonmal[i][j])
            nonrst += 1

print(norrst, nonrst)
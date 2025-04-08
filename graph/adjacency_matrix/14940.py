''' [쉬운 최단거리]
역발상
각 지점부터 시작하는 것이 아닌, 2가 있는 지점부터 시작
'''

from collections import deque
import sys
input = sys.stdin.readline

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

# N: 세로, M: 가로
N, M = map(int, input().split())
am = [list(map(int, input().split())) for _ in range(N)]
rst = [[-1] * M for _ in range(N)] # 못가면 -1
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if am[i][j] == 2:
            sy, sx = i, j
            break
    else:
        continue
    break

q = deque()
q.append((sy, sx))
rst[sy][sx] = 0
visited[sy][sx] = True

while q:
    y, x = q.popleft()
    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and am[ny][nx] == 1:
                visited[ny][nx] = True
                rst[ny][nx] = rst[y][x] + 1
                q.append((ny, nx))

for row in range(N):
    for col in range(M):
        if am[row][col] == 0:
            rst[row][col] = 0

for row in rst:
    print(*row)
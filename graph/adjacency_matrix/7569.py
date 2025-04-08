''' [토마토]
7576 문제의 응용문제
'''

from collections import deque

# M: 가로, N: 세로, H: 높이
# 상하좌우 위 아래 이동
dy = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)
M, N, H = map(int, input().split())

# 입력과 동시에 익은 토마토를 초기 탐색 대상에 삽입
q = deque()
box = []
for h in range(H):
    surface = []
    for n in range(N):
        row = list(map(int, input().split()))
        surface.append(row)
        for m in range(M):
            if row[m] == 1:
                q.append((h, n, m))
    box.append(surface)

def bfs():
    while q:
        z, y, x = q.popleft()
        for direction in range(6):
            nz = z + dz[direction]
            ny = y + dy[direction]
            nx = x + dx[direction]

            if 0 <= nz < H \
            and 0 <= ny < N \
            and 0 <= nx < M:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    q.append((nz, ny, nx))

bfs()

def get_day():
    rst = 0
    for surface in box:
        for row in surface:
            if 0 in row:
                return -1
            
            row_max = max(row)
            if rst < row_max:
                rst = row_max

    return rst - 1

print(get_day())
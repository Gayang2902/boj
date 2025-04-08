''' [토마토]
'''

from collections import deque

# M: 가로, N: 세로
M, N = map(int, input().split())
q = deque()
tomatoes = []
# 입력과 동시에 익은 토마토를 초기 탐색 대상에 삽입
for i in range(N):
    row = list(map(int, input().split()))
    tomatoes.append(row)
    for j in range(M):
        if row[j] == 1:
            q.append((i, j))

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = tomatoes[y][x] + 1
                q.append((ny, nx))
bfs()

def get_day():
    rst = 0
    for row in tomatoes:
        if 0 in row:
            return -1
        
        row_max = max(row)
        if rst < row_max:
            rst = row_max
    
    return rst - 1 #> 문제에서 요구하는 것은 몇 일이 지났는지에 대한 것

print(get_day())
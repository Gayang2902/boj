'''
아래 형태의 지도가 있다고 가정
 	0 	1 	2 	3 	4 	5
0 		1 	1 	1 	1 	1
1 		1 				1
2 		1 		1 		1
3 		1 		1 		
4 				1 	1 	
5 	1 	1 	1 	1 	1 	
----
6 6
0 1 1 1 1 1
0 1 0 0 0 1
0 1 0 1 0 1
0 1 0 1 0 0 
0 0 0 1 1 0
1 1 1 1 1 0
'''

# 입력
N, M = map(int, input().split())
a = []
for _ in range(N):
    row = list(map(int, input().split()))
    a.append(row)

# 입력 확인
for row in a:
    print(row)

visited = [[False] * M for _ in range(N)]
# 여기서는 상하좌우 순으로 이동
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
# DFS의 함수 구현
def dfs(y, x):    
    print(y, x)
    # 첫 시작
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i] # nexy y
        nx = x + dx[i] # nexy x

        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if a[ny][nx] == 1:
            continue
        if not visited[ny][nx]:
            dfs(ny, nx)

dfs(0, 0)

# BFS의 함수 구현
from collections import deque
def bfs(y, x):
    visited = [[False] * M for _ in range(N)]
    # 상하좌우
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    visited[y][x] = True
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        print(y, x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if a[ny][nx] == 1:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
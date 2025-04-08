''' [미로 탐색]
모든 DFS 문제는 BFS로 해결할 수 있지만, 역은 성립하지 않음
- 최소의 칸 수를 구해야 하는 경우가 이에 해당
BFS로 탐색 시에는 방문 순서가 너비로 되기 때문에 어떤 위치에 처음 도달한 시기가 가장 빠른 경로임
- 문제에서 `최소` 라는 단어가 보이면 BFS를 고려
- 같은 거리의 노드를 한 번에 탐색하기 때문
'''

from collections import deque

N, M = map(int, input().split())
a = [input().strip() for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
def bfs():
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))

    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue

            if a[ny][nx] == '1' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

bfs()
print(visited[N - 1][M - 1])
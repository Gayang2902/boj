''' [섬의 개수]
연결된 섬이 몇개 있는지 알아내는 문제기 때문에 BFS가 아닌 간단한 DFS로 구현
- 가로, 세로, 대각선으로 이동할 수 있음을 유의

새로운 땅의 일부분을 발견하면 해당 지역에 대해 DFS로 모든 구역을 탐색하여 방문기록에 체크
'''

import sys
# w, h는 50 이하이기 때문에 50 * 50 = 2,500 내외의 재귀에서 해결 가능
sys.setrecursionlimit(10 ** 4)

# 상하좌우 + 대각선
dy = (-1, 1, 0, 0, -1, -1, 1, 1)
dx = (0, 0, -1, 1, -1, 1, -1, 1)
def dfs(y, x):
    # 탐색한 땅은 바다로 취급
    m[y][x] = 0
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if m[ny][nx]:
                dfs(ny, nx)

while True:
    # width, height
    w, h = map(int, input().split())
    if not (w and h):
        break

    m = [list(map(int, input().split())) for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if m[i][j]: # 땅이 있고, 방문하지 않았다면...
                dfs(i, j) # 해당 섬에서 연결된 곳을 DFS로 탐색 (덩어리 탐색)
                cnt += 1

    print(cnt)
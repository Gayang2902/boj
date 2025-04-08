'''
[입력]
정점의 개수
간선의 개수
연결된 노드들...
5
8
1 2
1 3
1 5
2 3
2 5
3 4
3 5
4 5
'''

# 인접 `리스트` 생성
N = int(input()) # node
M = int(input()) # edge
a = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# DFS
visited = [False] * (N + 1)
def dfs(node):
    print(node)
    visited[node] = True
    for i in a[node]:
        if not visited[i]:
            dfs(i)
dfs(1)

# BFS
from collections import deque
def bfs(start):
    visited = [False] * (N + 1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        print(node)
        for i in a[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
bfs(1)
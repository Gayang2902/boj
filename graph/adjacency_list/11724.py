''' [연결 요소의 개수]
연결 요소 개수 찾기의 가장 기본적인 문제
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# N: node, M: edge
N, M = map(int, input().split())
a = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

visited = [False] * (N + 1)
def dfs(node):
    visited[node] = True
    for node_n in a[node]:
        if not visited[node_n]:
            dfs(node_n)

cnt = 0
for n in range(1, N + 1):
    if not visited[n]:
        dfs(n)
        cnt += 1
print(cnt)

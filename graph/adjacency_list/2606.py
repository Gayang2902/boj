''' [바이러스]
인접 행렬에서 연결 요소의 수를 찾는 문제
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
M = int(input())
m = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    m[u].append(v)
    m[v].append(u)  

cnt = -1
visited = [False] * (N + 1)
def dfs(node):
    global cnt
    visited[node] = True
    cnt += 1
    for node_n in m[node]:
        if not visited[node_n]:
            dfs(node_n)

dfs(1)
print(cnt)
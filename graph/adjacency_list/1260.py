''' [DFS와 BFS]
'''

from collections import deque
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(x + '\n')

N, M, V = map(int, input().split())
am = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    am[u].append(v)
    am[v].append(u)
for a in am:
    a.sort() # 문제에서 요구하는 탐색 순서를 맞추기 위함

visited = [False] * (N + 1)
def dfs(node):
    visited[node] = True
    rst.append(str(node))
    
    for node_n in am[node]:
        if not visited[node_n]:
            dfs(node_n)

def bfs(node):
    visited = [False] * (N + 1)
    q = deque([node])
    visited[node] = True
    rst.append(str(node))

    while q:
        node = q.popleft()
        
        for n in am[node]:
            if not visited[n]:
                visited[n] = True
                rst.append(str(n))
                q.append(n)

rst = []
dfs(V)
print(' '.join(rst))
rst = []
bfs(V)
print(' '.join(rst))
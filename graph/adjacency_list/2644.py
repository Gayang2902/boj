''' [촌수계산]
촌수계산이므로 BFS를 사용하여 최소경로를 계산
- 하지만 이 문제에서는 부모가 1명이라는 전제가 있음 -> 사이클이 존재하지 않음
- 부모가 1명이라면, 순환 그래프가 될 수 없기 때문에 DFS로 풀어도 무방
부모가 1명이라는 전제가 없다면, BFS로 풀어도 그것이 정답이 아닐 수 있음
- `DFS로 풀리는 모든 문제는 BFS로 풀 수 있다. 역은 성립하지 않는다.`
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
m = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    m[u].append(v)
    m[v].append(u)

def bfs(start, end):
    visited = [-1] * (N + 1)
    q = deque([start])
    visited[start] = 0 # 시작점(자기자신)은 0촌

    while q:
        node = q.popleft()

        for n in m[node]:
            if visited[n] == -1:
                visited[n] = visited[node] + 1 # 촌수가 1씩 늘어남
                q.append(n)

    return visited[end] # 못만나면 -1촌
    
print(bfs(a, b))
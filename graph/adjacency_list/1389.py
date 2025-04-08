''' [케빈 베이컨의 6단계 법칙]
'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    m[u].append(v)
    m[v].append(u)

def bfs(start):
    visited = [-1] * (N + 1)
    visited[start] = 0
    q = deque([start])
    
    while q:
        node = q.popleft()
        for n in m[node]:
            if visited[n] == -1:
                visited[n] = visited[node] + 1
                q.append(n)
    
    return sum(visited[1:]) # 입력받은 그래프는 연결 그래프

def baken():
    rst = []
    for i in range(1, N + 1):
        rst.append((bfs(i), i))

    rst.sort()
    return rst[0][1]

print(baken())
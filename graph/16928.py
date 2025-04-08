''' [뱀과 사다리 게임]
사다리나 뱀에 도착하면 `자동 이동`

풀이시간: 45분
'''

from collections import deque
import sys
input = sys.stdin.readline

path = [i for i in range(101)]

N, M = map(int, input().split())

for l in range(N):
    fr, to = map(int, input().split())
    path[fr] = to

for s in range(M):
    fr, to = map(int, input().split())
    path[fr] = to

for i in range(1, 101):
    if path[i]:
        continue
    for j in range(1, 7):
        path[i].append(i + j)

def bfs():
    visited = [-1] * (101)
    visited[1] = 0
    q = deque([1])

    while q:
        cur = q.popleft()

        for dice in range(1, 7):
            nxt = cur + dice
            if nxt > 100:
                continue

            dst = path[nxt]

            if visited[dst] == -1:
                visited[dst] = visited[cur] + 1
                q.append(dst)

    return visited[100]

print(bfs())
''' [헌내기는 친구가 필요해]
'''

from collections import deque

N, M = map(int, input().split())

am = []
people = []
for n in range(N):
    inp = list(input())
    if 'I' in inp:
        doyeon = (n, inp.index('I'))
    elif 'P' in inp:
        people.append((n, inp.index('P')))
    am.append(inp)

def bfs(doyeon):
    start_y, start_x = doyeon

    visited = [[False] * M for _ in range(N)]
    visited[start_y][start_x] = True
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    cnt = 0

    q = deque([(start_y, start_x)])
    
    while q:
        y, x = q.popleft()
        if am[y][x] == 'P':
           cnt += 1 
        for direction in range(4):
            ny = y + dy[direction]
            nx = x + dx[direction]

            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if visited[ny][nx] or am[ny][nx] == 'X':
                continue
            visited[ny][nx] = True
            q.append((ny, nx))
    
    return cnt

rst = bfs(doyeon)
print(rst if rst > 0 else 'TT')
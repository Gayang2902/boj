''' [DSLR]
풀이 시간: 46분
'''

from collections import deque

D = lambda x: (x * 2) % 10000
S = lambda x: 9999 if x == 0 else x - 1
L = lambda x: (x % 1000) * 10 + x // 1000
R = lambda x: (x % 10) * 1000 + x // 10

cmd = [[D, 'D'], [S, 'S'], [L, 'L'], [R, 'R']]

def bfs(start, dst):
    visited = [''] * 10000
    visited[start] = ''
    q = deque([start])

    while q:
        chk = q.popleft()
        if chk == dst:
            return visited[chk]
        
        for c in cmd:
            nxt = c[0](chk)

            if visited[nxt] == '':
                visited[nxt] = visited[chk] + c[1]
                q.append(nxt)

T = int(input())
for tc in range(T):
    print(bfs(*map(int, input().split())))
''' [숨바꼭질]
찾을 수 있는 가장 `빠른` 시간 -> BFS로 구현
BFS의 본질을 이해하기 좋은 문제?
'''

from collections import deque

N, K = map(int, input().split())
MAX = (100000 + 1)
line = [0] * MAX
def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        if x == K:
            print(line[x])
            return
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and line[nx] == 0:
                line[nx] = line[x] + 1
                q.append(nx)

bfs(N)
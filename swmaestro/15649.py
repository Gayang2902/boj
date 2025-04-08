''' [N과 M (1)]
백트래킹 / DFS
'''

N, M = map(int, input().split())

l = []
visited = [False] * (N + 1)

from itertools import permutations
nums = [i for i in range(1, N + 1)]
good = permutations(nums, M)
for i in good:
    print(*i)

def dfs():
    if len(l) == M:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        l.append(i)
        dfs()
        l.pop()
        print(l)
        print(visited)
        visited[i] = False

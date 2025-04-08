''' [N과 M (9)]
'''

N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

rst = []
visited = [False] * N
def dfs(depth):
    if depth == M:
        print(*rst)
        return
    
    prev = set()
    for i in range(N):
        if not visited[i] and l[i] not in prev:
            visited[i] = True
            rst.append(l[i])
            prev.add(l[i])

            dfs(depth + 1)

            visited[i] = False
            rst.pop()

dfs(0)
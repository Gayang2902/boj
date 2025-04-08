''' [N과 M(1)]
순열이 아닌 백트래킹을 사용하여 풀이
'''

N, M = map(int, input().split())

visited = [False] * (N + 1)
rst = []
def dfs(depth):
    if depth == M:
        print(*rst)
        return
    
    for i in range(1, N + 1):
        if visited[i]:
            continue

        visited[i] = True
        rst.append(i)

        dfs(depth + 1)

        visited[i] = False
        rst.pop()
dfs(0)
''' [N과 M(2)]
N과 M(1)과 유사하지만 중복을 허용하지 않음
'''

N, M = map(int, input().split())

visited = [False] * (N + 1)
rst = []
def dfs(start):
    if len(rst) == M:
        print(*rst)
        return
    
    for i in range(start, N + 1):
        if visited[i]:
            continue

        visited[i] = True
        rst.append(i)

        dfs(i + 1)

        visited[i] = False
        rst.pop()
dfs(1)
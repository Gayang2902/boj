''' [N과 M (4)]
'''

N, M = map(int, input().split())
visited = [0]
rst = []

def dfs(prev):
    if len(rst) == M:
        print(*rst)
        return
    
    for i in range(1, N + 1):
        if visited[-1] > i:
            continue

        visited.append(i)
        rst.append(i)
        dfs(prev + 1)
        visited.pop()
        rst.pop()

dfs(1)
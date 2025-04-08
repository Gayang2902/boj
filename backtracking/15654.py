''' [N과 M (5)]
'''

N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

visited = []
rst = []
def dfs():
    if len(rst) == M:
        print(*rst)
        return
    
    for i in l:
        if i in visited:
            continue

        visited.append(i)
        rst.append(i)

        dfs()

        visited.pop()
        rst.pop()

dfs()
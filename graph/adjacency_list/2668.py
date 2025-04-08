''' [숫자고르기]
어떤 정점을 골랐을 때, 순환 그래프에 속한다면 집합에 추가
- DFS로 탐색했을 때, 자기 자신으로 돌아온다면 순환 그래프의 일부분
'''

N = int(input())
m = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    v = int(input())
    m[v].append(i)

rst = []
def dfs(start, n):
    visited[n] = True

    for node in m[n]:
        if not visited[node]:
            dfs(start, node)
        elif start == node: # 다음 탐색 지역이 나 자신이면 순환 그래프!!!
            rst.append(start)
            return

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

rst.sort()
print(len(rst))
print('\n'.join(map(str, rst)))
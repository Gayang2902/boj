''' [경로 찾기]
'''

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# i->k, k->j면 i->j도 가능
for k in range(N): # 중간
    for i in range(N): # 시작
        for j in range(N): # 도착
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(' '.join(map(str, row)))
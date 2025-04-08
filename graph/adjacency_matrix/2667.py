''' [단지번호붙이기]
인접행렬 형태의 DFS 문제
'''

N = int(input())
m = [list(input().strip()) for _ in range(N)]

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)
def dfs(i, j):
    m[i][j] = '0'
    cnt = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and m[ni][nj] == '1':
            cnt += dfs(ni, nj)
    
    return cnt

rst = []
for i in range(N):
    for j in range(N):
        if m[i][j] == '1':
            cnt = dfs(i, j)
            rst.append(cnt)

print(rst.__len__())
print('\n'.join(map(str, sorted(rst))))
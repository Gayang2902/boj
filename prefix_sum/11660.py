''' [구간 합 구하기 5]
'''

import sys

def mii():
    return map(int, sys.stdin.readline().split())

N, M = mii()

mat = [0] + [[0] + list(mii()) for _ in range(N)]
pre_sum_mat = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        pre_sum_mat[i][j] = mat[i][j]
        pre_sum_mat[i][j] += pre_sum_mat[i][j - 1] + pre_sum_mat[i - 1][j]
        pre_sum_mat[i][j] -= pre_sum_mat[i - 1][j - 1]

result = []
for _ in range(M):
    x1, y1, x2, y2 = mii()
    ans = pre_sum_mat[x2][y2]
    ans -= pre_sum_mat[x2][y1 - 1]
    ans -= pre_sum_mat[x1 - 1][y2]
    ans += pre_sum_mat[x1 - 1][y1 - 1]
    result.append(ans)

sys.stdout.write('\n'.join(map(str, result)) + '\n')
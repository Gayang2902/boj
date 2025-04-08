''' [구간 합 구하기 4]
'''

import sys

def mii():
    return map(int, sys.stdin.readline().split())

N, M = mii()
nums = [0] + list(mii())
pre_sum = [0] * (N + 1)

for i in range(1, N + 1):
    pre_sum[i] = pre_sum[i - 1] + nums[i]

result = []
for _ in range(M):
    i, j = mii()
    result.append(pre_sum[j] - pre_sum[i - 1])

sys.stdout.write('\n'.join(map(str, result)) + '\n')
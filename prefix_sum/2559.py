''' [수열]
'''

import sys

N, K = map(int, sys.stdin.readline().split())
days = list(map(int, sys.stdin.readline().split()))

ps = []
tmp = 0
for d in days:
    tmp += d
    ps.append(tmp)

result = ps[K - 1]
for i in range(K, N):
    tmp = ps[i] - ps[i - K]
    result = max(result, tmp)

print(result)

# 슬라이딩 윈도우로 푸는 방법
def sliding_window(N, K, days):
    result = sum(days[:K])

    tmp = result
    for i in range(K, N):
        tmp += days[i] - days[i - K]
        result = max(result, tmp)    
    
    return result
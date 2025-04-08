''' [수열]
'''

N, K = map(int, input().split())
days = list(map(int, input().split()))

# 최초 윈도우 생성
sw = sum(days[:K])
m = sw

# 윈도윙
for i in range(K, N):
    sw += days[i] - days[i - K]
    m = max(m, sw)

print(m)
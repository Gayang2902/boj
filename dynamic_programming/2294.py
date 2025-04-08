''' [동전 2]
동전의 개수가 무한대
동전의 최소 개수를 구하는 것
'''

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
dp = [10001 for i in range(K + 1)]
dp[0] = 0

for c in coin:
    for i in range(c, K + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
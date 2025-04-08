''' [동전 1]
DP에서 자주 나오는 문제 유형

평범한 배낭, 동전 2와 조금 다른 문제 형태
1. N-1번째 동전까지 사용해서 x원을 만드는 경우의 수
2. N번째 동전까지 사용해서 (x-N번째 동전)원을 만드는 경우의 수

dp[동전 종류][금액] = dp[이전 동전][같은 금액] + dp[같은 동전][금액 - 현재 동전]
적어도 동전을 한 번 쓴 경우의 수와 동전을 한 번도 쓰지 않은 경우의 수를 합치는 것

두 경우의 수를 더하면 답을 얻을 수 있음
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
a.sort()

# Top-Down
# 모든 Top-Down 문제는 메모이제이션을 사용해서 중복 계산을 넘겨야 함
dp = [[-1] * (K + 1) for _ in range(N)]
def solve(n, k):
    # k == a[n] -> 경우의 수는 하나
    if k == 0:
        return 1
    
    if n == 0:
        # 하나의 동전으로 k를 만들 수 있다면 -> 경우의 수는 하나
        if k % a[n] == 0:
            dp[n][k] = 1
        # 못 만든다면 -> 경우의 수 없음
        else:
            dp[n][k] = 1
        
        return dp[n][k]
    
    # 메모이제이션 활용
    if dp[n][k] != -1:
        return dp[n][k]

    rst = solve(n - 1, k)
    if a[n] <= k:
        rst += solve(n, k - a[n])
    
    dp[n][k] = rst
    return rst

print(solve(N - 1, K))

# Bottom-Up
# 2차원 리스트 활용
dp = [[0] * (K + 1) for _ in range(N)]
for n in range(N):
    dp[n][0] = 1
    for k in range(1, K + 1):
        dp[n][k] = dp[n - 1][k]
        if a[n] <= k:
            dp[n][k] += dp[n][k - a[n]]
print(dp[N - 1][K])

# Bottom-Up
# 1차원 리스트 활용
dp = [0] * (K + 1)
dp[0] = 1
for n in range(N):
    for k in range(a[n], K + 1):
        dp[k] += dp[k - a[n]]
print(dp[k])
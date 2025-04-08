''' [2xn 타일링]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 1000, 'Out of range'

    dp = [0 for i in range(N + 2)]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N] % 10007

print(solution())


''' [2xn 타일링]
피보나치 수열의 점화식인
F_n = F_{n - 1} + F_{n - 2} 와 일치
'''

# Top-Down
N = int(input())
MOD = 10007
memo = [0 for _ in range(N + 1)]

def F(n):
    if n <= 2:
        return n
    if memo[n] > 0:
        return memo[n]
    
    memo[n] = F(n - 1) + F(n - 2)
    memo[n] %= MOD

    return memo[n]

print(F(N))
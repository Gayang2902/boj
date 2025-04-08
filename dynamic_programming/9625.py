''' [BABBA]
A -> B
B -> BA
이 문제도 결국 피보나치와 유사
A = Fibo(K - 1)
B = Fibo(K)
'''

# Bottom-Up
K = int(input())
dp = [0] * (K + 1)
dp[1] = 1

for i in range(2, K + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[K - 1], dp[K])
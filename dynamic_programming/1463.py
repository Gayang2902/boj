''' [1로 만들기]
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 10**6, 'Out of range'

    # 최소 연산 횟수를 배열에 저장
    dp = [0 for i in range(N + 1)]
    
    for i in range(2, N + 1):
        # 1을 빼는 경우는 무조건 가능
        # 이후 2 또는 3의 배수라면 나눠서 가는 경우와 비교
        dp[i] = dp[i - 1] + 1

        # 2로 나눌 수 있는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 3으로 나눌 수 있는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[N]
    
print(solution())
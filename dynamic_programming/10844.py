''' [쉬운 계단 수]
'''

# a_i = a_i-1 * 2 - 1

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 100, 'Out of range'

    dp = [[0 for i in range(10)] for j in range(101)]
    print(dp)
    dp[1][1:10] = [1] * 9
    
    for digit in range(2, N + 1):       # 자릿수
        for msb in range(10):           # MSB
            # 101처럼 0이 중간에 오는 경우가 있기 때문에 0으로 시작하는 숫자도 고려
            if msb == 0:
                dp[digit][msb] = dp[digit - 1][1]
            elif msb == 9:
                dp[digit][msb] = dp[digit - 1][8]
            else:
                dp[digit][msb] = dp[digit - 1][msb - 1] + dp[digit - 1][msb + 1]

    return sum(dp[N]) % 1000000000
            
sys.stdout.write(str(solution()) + '\n')
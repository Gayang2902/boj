''' [오르막 수]
'''

import sys

def solution(N: int) -> int:
    assert 1 <= N <= 1000, 'Out of range'

    cache = [[0 for i in range(10)] for j in range(N + 1)]
    cache[1] = [1] * 10

    for i in range(2, N + 1):
        for j in range(10):
            cache[i][j] = sum(cache[i - 1][j:])

    return sum(cache[N]) % 10007
            
print(solution(int(sys.stdin.readline())))
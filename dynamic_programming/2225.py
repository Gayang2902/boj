''' [합분해] @@@ 다시 풀어보기

4를 0~4까지의 수 2개로 만드는 법을 예시로 생각
4 = (0, 4)
    (1, 3)
    (2, 2)
    (3, 1)
    (4, 0)
4 = x + y -> x가 정해지면 y는 알아서 정해짐

cache[k][n] = cache[k - 1][0] + cache[k - 1][1] + ... + cache[k - 1][n]
cache[1][n] = 1
cache[0][n] = 0
cache[n][0] = 1

==>
cache[k - 1][0] + ... cache[k - 1][n - 1] = cache[k][n - 1]
==>
cache[k][n] = cache[k][n - 1] + cache[k - 1][n]
'''

import sys

def solution(N: int, K: int) -> int:
    assert 1 <= N <= 200, 'Out of range'
    assert 1 <= K <= 200, 'Out of range'

    cache = [[0] * (N + 1) for _ in range(K + 1)]

    # k개의 숫자로 0을 만드려면
    for k in range(0, K + 1):
        cache[k][0] = 1
    # 1개의 숫자로 n을 만드려면
    for n in range(0, N + 1):
        cache[1][n] = 1

    for k in range(2, K + 1):
        for n in range(1, N + 1):
            cache[k][n] = (cache[k][n - 1] + cache[k - 1][n]) % 1000000000

    return cache[K][N]


N, K = map(int, sys.stdin.readline().split())
print(solution(N, K))
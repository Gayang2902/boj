''' [2xn 타일링 2]
'''

# a_i = a_i-2 * 2 + a_i-1

import sys

def solution():
    N = int(sys.stdin.readline())
    assert 1 <= N <= 1000, 'Out of range'

    cache = [0 for i in range(N + 4)]
    cache[1] = 1
    cache[2] = 3
    cache[3] = 5
    cache[4] = 11

    for i in range(5, N + 1):
        cache[i] = cache[i - 2] * 2 + cache[i - 1]

    return cache[N] % 10007

print(solution())
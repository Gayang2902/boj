''' [포도주 시식]
1. 현재 잔을 마신다.
    1.1. 이전 잔을 마셨다.          -> ai + ai-1 + dpi-3
    1.2. 이전 잔을 마시지 않았다.    -> ai + dpi-2
2. 현재 잔을 마시지 않는다.          -> dpi-1
'''

import sys

# Bottom-Up
def solution(N: int) -> int:
    assert 1 <= N <= 10000, 'Out of range'

    grapes = [int(sys.stdin.readline()) for _ in range(N)]

    if N == 1:
        return grapes[0]
    elif N == 2:
        return grapes[0] + grapes[1]
    
    cache = [0] * (N + 1)
    cache[1] = grapes[0]
    cache[2] = grapes[0] + grapes[1]
    
    for i in range(3, N + 1):
        gi = i - 1
        onedotone = grapes[gi] + grapes[gi - 1] + cache[i - 3]
        onedottwo = grapes[gi] + cache[i - 2]
        two       = cache[i - 1]
        cache[i] = max(onedotone, onedottwo, two)

    return max(cache)

N = int(sys.stdin.readline())
print(solution(N))

# Top-Down
N = int(input())
wine = [int(input()) for _ in range(N)]
memo = [-1] * N
def solve(N):
    if N == 0:
        return wine[0]
    elif N == 1:
        return wine[0] + wine[1]
    elif N == 2:
        return max(solve(1), max(wine[0], wine[1]) + wine[2])
    
    if memo[N] != -1:
        return memo[N]

    case1 = solve(N - 1)
    case2 = solve(N - 2) + wine[N]
    case3 = solve(N - 3) + wine[N - 1] + wine[N]    

    memo[N] = max(case1, case2, case3)
    return memo[N]
''' [연속합]
'''

import sys

def solution(N: int, seq: list) -> int:
    if N == 1:
        return seq[0]
    cache = seq[:]
    for i in range(1, N):
        if cache[i - 1] + seq[i] > seq[i]:
            cache[i] = cache[i - 1] + seq[i]

    return max(cache)


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
print(solution(N, seq))
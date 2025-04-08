''' [가장 긴 감소하는 부분 수열]
LDS, Longest Decreasing Subsequence
'''

import sys

def solution(N: int) -> int:
    seq = list(map(int, sys.stdin.readline().split()))
    if N == 1:
        return 1
    
    cache = [1] * N
    for i in range(1, N):
        for j in range(i):
            if seq[j] > seq[i]:
                cache[i] = max(cache[i], cache[j] + 1)

    return max(cache)

N = int(sys.stdin.readline())
print(solution(N))
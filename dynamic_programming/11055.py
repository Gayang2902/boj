''' [가장 큰 증가하는 부분 수열]
'''

import sys

def solution(N: int) -> int:
    seq = list(map(int, sys.stdin.readline().split()))

    if N == 1:
        return seq[0]
    
    cache = seq[:]
    
    for i in range(1, N):
        for j in range(i):
            if seq[j] < seq[i]:
                cache[i] = max(cache[i], cache[j] + seq[i])

    return max(cache)

N = int(sys.stdin.readline())
print(solution(N))
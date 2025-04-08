''' [가장 긴 증가하는 부분 수열]
Longest Increasing Subsequence
'''

import sys

def solution(N: int) -> int:
    assert 1 <= N <= 1000, 'Out of range'
    seq = list(map(int, sys.stdin.readline().split()))
    
    if N == 1:
        return 1
    elif N == 2:
        return 2 if seq[1] > seq[0] else 1
    
    cache = [1] * N
    cache[1] = 2 if seq[1] > seq[0] else 1
    for i in range(N):
        for j in range(i):
            # 현재 위치보다 낮은 위치들에서 최장 길이 수열 해를 탐색
            if seq[j] < seq[i]:
                cache[i] = max(cache[i], cache[j] + 1)

    return max(cache)    

N = int(sys.stdin.readline())
print(solution(N))
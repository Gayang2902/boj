''' [타일 채우기] @@@
3 x N 타일을 2x1, 1x2 크기의 타일로 채우는 경우의 수

기본 패턴: a_i-2 * 3
새로운 패턴: sum_{k=4}^{i}a_i-k * 2
스페셜 패턴: 2
'''

import sys

def solution(N: int) -> int:
    assert 1 <= N <= 30, 'Out of range'
    
    if N % 2 == 1:
        return 0
    cache = [0] * 31
    cache[2] = 3
    
    for i in range(4, N + 1, 2):
        cache[i] = cache[i - 2] * 3
        for j in range(4, i, 2):
            cache[i] += cache[i - j] * 2
        cache[i] += 2
    
    return cache[N]

N = int(sys.stdin.readline())
print(solution(N))
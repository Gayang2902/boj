''' [제곱수의 합]
N을 제곱수들의 합으로 표현했을 때, 필요한 항의 최소 개수

dp 문제에서는 cache[]에 존재하는 값은 최적의 해를 이미 구한 것이라는 명심
(이미 계산된 문제는 더 이상 계산할 필요 없음)
'''

import sys

def solution(N: int) -> int:
    cache = [i for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, i):
            if j * j > i:
                break
            # cache[i] = min(cache[i], cache[i - j * j ] + 1)
            if cache[i] > cache[i - j * j] + 1:
                cache[i] = cache[i - j * j] + 1

    return cache[N]
    
N = int(sys.stdin.readline())
print(solution(N))
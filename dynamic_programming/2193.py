''' [이친수]
* 0과 1로만 이루어진 수 중에서,
1. 이친수는 0으로 시작하지 않는다.
2. 이친수는 1이 두 번 연속으로 나타나지 않는다. (11을 부분집합으로 가지지 않음)
'''

# d[i] = d[i - 2] + d[i - 1]

import sys

def solution(N: int) -> int:
    assert 1 <= N <= 90, 'Out of range'

    cache = [[0 for i in range(10)] for j in range(N + 1)]
    cache[1][1] = 1

    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                cache[i][0] = cache[i - 1][1] + cache[i - 1][0]
            elif j == 1:
                cache[i][1] = cache[i - 1][0]

    return sum(cache[N])

def solution2(N: int) -> int:
    cache = [0] * (N + 1)
    cache[1] = 1
    for i in range(2, N + 1):
        cache[i] = cache[i - 2] + cache[i - 1]
    return cache[N]

N = int(sys.stdin.readline())
print(solution(N))
print(solution2(N))

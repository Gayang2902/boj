'''[분해합]
주어진 자연수 N의 가장 작은 생성자를 구하는 알고리즘
'''

import sys

def solution():
    N = int(sys.stdin.readline())
    # 전제 조건
    assert 1 <= N <= 1000000, 'Out of Range'
    
    # gs = list()
    # for i in range(1, N):

    # g의 최솟값은 `N - 9 * (N의 자릿수)` 이상
    start = max(1, N - 9 * len(str(N)))
    for g in range(start, N):
        # g = N - i
        # sg = sum(list(map(int, list(str(g)))))
        sg = sum(int(d) for d in str(g))
        if g + sg == N:
            return g

    return 0
    # return gs[len(gs) - 1] if len(gs) else 0

def good():
    N = int(sys.stdin.readline())
    start = max(1, N - 9 * len(str(N)))
    for g in range(start, N):
        if g + sum(int(d) for d in str(g)) == N:
            return g
    return 0

print(solution())
print(good())
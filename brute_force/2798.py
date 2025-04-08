'''[블랙잭]
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
'''

import sys

## O(N^3)
def solution():
    N, M = map(int, sys.stdin.readline().split())
    # 전제 조건
    # assert 3 <= N <= 100 and 10 <= M <= 3000000, 'Out of Range'
    
    cards = list(map(int, sys.stdin.readline().split()))
    # assert len(cards) == N, 'need N values'
    cards.sort(reverse=True)
    m = 0

    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                s = cards[i] + cards[j] + cards[k]
                if s <= M:
                    m = max(m, s)

    return m


from itertools import combinations
def solve():
    N, M = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    m = 0

    for selected_card in combinations(a, 3):
        s = sum(selected_card)
        if m < s <= M:
            m = s

    return m

print(solution())
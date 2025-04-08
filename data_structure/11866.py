''' [요세푸스 문제]
'''

# 큐를 이용해서 구현
from collections import deque

import sys

def solution(N: int, K: int) -> list:
    queue = deque(range(1, N + 1))
    ans = list()

    while queue:
        cnt = 1
        while cnt < K:
            t = queue.popleft()
            queue.append(t)
            cnt += 1
        ans.append(queue.popleft())

    return ans

N, K = map(int, sys.stdin.readline().split())
sys.stdout.write('<' + ', '.join(str(i) for i in solution(N, K)) + '>\n')
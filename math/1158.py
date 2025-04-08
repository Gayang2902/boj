''' [요세푸스 문제]
'''

from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N + 1)])

rst = []
while dq:
    for i in range(K - 1):
        dq.append(dq.popleft())

    rst.append(dq.popleft())

print('<' + ', '.join(map(str, rst)) + '>')
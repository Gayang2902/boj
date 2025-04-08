''' [카드2]
'''

from collections import deque

N = int(input())
dq = deque([i for i in range(1, N + 1)])

while True:
    if len(dq) == 1:
        print(dq.popleft())
        break
    else:
        dq.popleft()
        dq.append(dq.popleft())
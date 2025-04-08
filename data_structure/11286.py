''' [절댓값 힙]
'''

import heapq
push = heapq.heappush
pop  = heapq.heappop

N = int(input())
h = []
d = dict()
rst = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if len(h) == 0:
            rst.append(0)
        else:
            rst.append(pop(d[pop(h)]))
    else:
        a = abs(x)
        push(h, a)
        if a not in d.keys():
            d[a] = [x]
        else:
            push(d[a], x)

print('\n'.join(map(str, rst)))
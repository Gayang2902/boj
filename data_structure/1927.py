''' [최소 힙]
'''

import heapq
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')

hq = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        print(0 if len(hq) == 0 else heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)
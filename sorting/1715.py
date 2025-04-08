''' [카드 정렬하기]
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
    heapq.heappush(h, int(input()))

rst = 0
while len(h) > 1:
    f = heapq.heappop(h)
    s = heapq.heappop(h)

    cost = f + s
    rst += cost

    heapq.heappush(h, cost)

print(rst)
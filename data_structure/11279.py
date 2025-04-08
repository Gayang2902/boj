''' [최대 힙]
'''

import heapq
import sys

def solution(N: int) -> None:
    heap = list()

    for _ in range(N):
        d = int(sys.stdin.readline())

        if d:
            heapq.heappush(heap, -d)
        else:
            if len(heap):
                t = heapq.heappop(heap)
                sys.stdout.write(str(-t) + '\n')
            else:
                sys.stdout.write(str(0) + '\n')

N = int(sys.stdin.readline())
solution(N)
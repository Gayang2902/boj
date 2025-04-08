''' [이중 우선순위 큐]
최대힙, 최소힙 두 개를 만들어서 삽입
- 두 힙에서 값을 빼낼 때 동기화를 위해 꼭 조건부 루프로 처리해야 함
- 이를 위해선 값의 삭제를 추적하는 매핑이 필수
'''

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_h = []
    min_h = []
    entry_cnt = defaultdict(int) # 삭제 추적용

    k = int(input())

    for cmd in range(k):
        oper, n = input().split()
        n = int(n)

        if oper == 'I':
            heapq.heappush(max_h, -n)       # 최대 힙
            heapq.heappush(min_h, n)        # 최소 힙
            entry_cnt[n] += 1
        else:
            if n == 1:
                while max_h:
                    max_n = -heapq.heappop(max_h)
                    if entry_cnt[max_n] > 0:
                        entry_cnt[max_n] -= 1
                        break
            else:
                while min_h:
                    min_n = heapq.heappop(min_h)
                    if entry_cnt[min_n] > 0:
                        entry_cnt[min_n] -= 1
                        break

    max_rst, min_rst = None, None

    while max_h:
        n = -heapq.heappop(max_h)
        if entry_cnt[n] > 0:
            max_rst = n
            break
    while min_h:
        n = heapq.heappop(min_h)
        if entry_cnt[n] > 0:
            min_rst = n
            break

    if max_rst is None or min_rst is None:
        print('EMPTY')
    else:
        print(max_rst, min_rst)

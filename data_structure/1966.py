''' [프린터 큐]
'''

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    impr = deque(list(map(int, input().split())))

    rst = 1
    while impr:
        if impr[0] < max(impr):
            impr.append(impr.popleft())
        else:
            if M == 0:
                break
            impr.popleft()
            rst += 1

        # 맨 뒤로 갔는지 판단
        M = M - 1 if M > 0 else len(impr) - 1

    print(rst)
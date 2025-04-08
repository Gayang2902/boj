''' [터렛]
'''

import sys
from math import sqrt

def solution() -> int:
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    # 두 점의 거리를 피타고라스 정리로 계산
    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    diffrence = abs(r1 - r2)
    
    # 두 원이 일치 -> 적의 위치가 무한대
    if distance == 0 and r1 == r2:
        return -1
    # 두 원이 외접하거나 내접 -> 적의 위치는 하나
    elif distance == r1 + r2 or distance == diffrence:
        return 1
    # 적의 위치가 둘
    elif diffrence < distance < r1 + r2:
        return 2
    else:
        return 0

T = int(sys.stdin.readline())
sys.stdout.write('\n'.join(str(solution()) for _ in range(T)) + '\n')

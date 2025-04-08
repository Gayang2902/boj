''' [계단 오르기]
1. 이전 계단을 밟았을 경우 -> a_i + a_i-1 + cache[i - 3]
2. 이전 계단을 밟지 않았을 경우 -> a_i + cache[i - 2]
'''

import sys

def solution(N: int, stairs: list) -> int:
    if N == 1:
        return stairs[0]
    elif N == 2:
        return stairs[0] + stairs[1]
    elif N == 3:
        return stairs[2] + max(stairs[0], stairs[1])
    
    # 무조건 현재 위치는 밟아야하기 때문에 굳이 메모이제이션을 위해 리스트는 필요없음
    prev_2 = stairs[0]
    prev_1 = stairs[0] + stairs[1]
    cur = stairs[2] + max(stairs[0], stairs[1])
    for i in range(3, N):
        new = max(stairs[i] + stairs[i - 1] + prev_2, stairs[i] + prev_1)
        prev_2, prev_1, cur = prev_1, cur, new
        
    return cur

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
print(solution(N, stairs))
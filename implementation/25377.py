''' [빵]
'''

import sys

def solution(N):
    MAX = 1001 # 빵이 나오는 시간 B: 1 <= B <= 1000
    rst = MAX
    for _ in range(N):
        A_time, B_time = map(int, sys.stdin.readline().split())
        if B_time < A_time:
            continue
        if B_time < rst:
            rst = B_time

    return -1 if rst == MAX else rst

N = int(sys.stdin.readline())   
sys.stdout.write(str(solution(N)) + '\n')
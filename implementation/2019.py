''' [막대기
'''

import sys

def solution(N: int, sticks: list) -> int:
    rst = 1
    m = sticks[N - 1]
    for stick in sticks[:-1][::-1]:
        if stick > m:
            rst += 1
            m = stick

    return rst

N = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for _ in range(N)]
sys.stdout.write(str(solution(N, sticks)) + '\n')
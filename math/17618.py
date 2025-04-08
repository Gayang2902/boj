''' [신기한 수]
'''

import sys

def solution(N: int) -> int:
    ns = 0

    for i in str(N):
        ns += int(i)
    if N % ns == 0:
        return True
    return False

N = int(sys.stdin.readline())
sys.stdout.write(str(sum([solution(i) for i in range(1, N + 1)])) + '\n')
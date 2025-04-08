''' [369]
'''

import sys

def solution(N: int) -> int:
    r = 0

    for i in range(1, N + 1):
        num = i
        while num:
            c = num % 10
            num //= 10

            if c == 3 or c == 6 or c == 9:
                r += 1
    return r

N = int(sys.stdin.readline())
sys.stdout.write(str(solution(N)) + '\n')
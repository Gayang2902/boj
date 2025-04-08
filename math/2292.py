'''[벌집]
'''

import sys

def solution(N: int) -> int:
    cnt = 1
    ret = 1
    
    while cnt < N:
        cnt += ret * 6
        ret += 1

    return ret


N = int(sys.stdin.readline())
sys.stdout.write(str(solution(N)) + '\n')
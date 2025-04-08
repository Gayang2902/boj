''' [파도반 수열]
'''

import sys

def solution(N: int, tc: list) -> int:
    m = max(tc)
    cache = [0] * (m + 1)
    cache[1], cache[2], cache[3] = 1, 1, 1
    if m >= 4:
        cache[4], cache[5] = 2, 2
    
    for i in range(6, m + 1):
        cache[i] = cache[i - 1] + cache[i - 5]

    sys.stdout.write('\n'.join(str(cache[x]) for x in tc) + '\n')

N = int(sys.stdin.readline())
tc = [int(sys.stdin.readline()) for _ in range(N)]
solution(N, tc)
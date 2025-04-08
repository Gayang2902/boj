''' [1, 2, 3 더하기]
'''

import sys

def solution():
    T = int(sys.stdin.readline())
    test_cases = [int(sys.stdin.readline()) for i in range(T)]

    cache = [0 for i in range(12)]
    cache[1] = 1
    cache[2] = 2
    cache[3] = 4
    cache[4] = 7

    for i in range(5, 12):
        if i - 1 > 0:
            cache[i] += cache[i - 1]
        if i - 2 > 0:
            cache[i] += cache[i - 2]
        if i - 3 > 0:
            cache[i] += cache[i - 3]
    
    output = [str(cache[i]) for i in test_cases]
    sys.stdout.write('\n'.join(output) + '\n')

solution()
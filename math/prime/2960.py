''' [에라토스테네스의 체] 
'''

import sys

def solution(N: int, K: int) -> int:
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False

    result = 0
    for i in range(2, N + 1):
        if prime[i] != False:
            for j in range(i, N + 1, i):
                if prime[j] == True:
                    prime[j] = False
                    result += 1

                    if result == K:
                        return j
                    
    return -1
                    
N, K = map(int, sys.stdin.readline().split())
sys.stdout.write(str(solution(N, K)) + '\n')
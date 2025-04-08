''' [가장 긴 바이토닉 부분 수열]

'''

import sys

def solution(N: int, seq: list) -> int:
    lis = [1] * N
    lds = [1] * N

    if N == 1:
        return 1
    
    # LIS
    for i in range(1, N):
        for j in range(i):
            if seq[j] < seq[i]:
                lis[i] = max(lis[i], lis[j] + 1)
    # LDS
    ## 일반적인 lDS 탐색이라면 순방향 탐색도 가능하지만, 바이토닉 수열을 구할 때는 역방향으로 탐색 
    ## (피봇이 존재하기 때문에)
    for i in range(N - 2, -1, -1):
        for j in range(i + 1, N):
            if seq[j] < seq[i]:
                lds[i] = max(lds[i], lds[j] + 1)
        
    result = 0
    for i in range(N):
        result = max(result, lis[i] + lds[i] - 1)
    return result

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
print(solution(N, seq))
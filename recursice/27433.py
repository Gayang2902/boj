''' [팩토리얼 2]
'''

import sys
''' BOJ 서버의 재귀는 1,000번으로 제한
    아래 함수를 호출하여 소스의 최대 재귀 깊이를 1,000,000으로 변경 
    채점 서버가 감당할 수 있는 최대 깊이는 10 ** 6 정도 '''
sys.setrecursionlimit(10 ** 6)

def solution(N: int) -> int:
    if N <= 1:
        return 1
    return N * solution(N - 1)

N = int(sys.stdin.readline())
sys.stdout.write(str(solution(N)) + '\n')
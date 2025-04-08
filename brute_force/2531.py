''' [회전초밥]
'''

import sys
from collections import defaultdict

def solution(N: list, d: int, k: int, c: int, sushis: list) -> int:
    max_sushi = 0
    for i in range(N):
        # 쿠폰의 초밥을 먼저 먹이고 시작
        check = [0] * (d + 1)
        check[c] = 1 
        eat_sushi = 1
        # 초밥을 연속해서 먹는 경우의 수 계산
        for j in range(i, i + k):
            sushi = sushis[j % N]

            if not check[sushi]:
                eat_sushi += 1
            check[sushi] += 1
        max_sushi = max(max_sushi, eat_sushi)
    
    return max_sushi    

# N: 접시의 수
# d: 초밥의 가짓수
# k: 연속해서 먹는 접시의 수
# c: 쿠폰 번호
N, d, k, c = map(int, sys.stdin.readline().split())
sushis = [int(sys.stdin.readline()) for _ in range(N)]
sys.stdout.write(str(solution(N, d, k, c, sushis)) + '\n')
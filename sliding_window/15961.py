''' [회전 초밥(어려운)]
2531과 같은 문제지만, N의 최대값이 3,000,000이 되었기 때문에
전체 반복횟수가 3,000,000 * 3,000으로 90억이기 때문에 브루트포싱이 불가능
'''

import sys

# N: 접시의 수, d: 초밥의 가짓수
# k: 연속해서 먹는 접시의 수, c: 쿠폰 번호
N, d, k, c = map(int, input().split())
l = [int(sys.stdin.readline()) for _ in range(N)]

check = [0] * (d + 1)
# 쿠폰에 해당하는 초밥은 이미 먹었다고 가정
check[c] = 1
eat_sushi = 1

# 최초 윈도우 생성
for i in range(k):
    sushi = l[i]

    # 이전에 먹은 초밥이 아니라면
    if check[sushi] == 0:
        eat_sushi += 1
    check[sushi] += 1

max_sushi = eat_sushi

for i in range(N):
    # 먹은 것에서 지울 초밥
    start = l[i]
    check[start] -= 1
    if check[start] == 0:
        eat_sushi -= 1

    # 새로 먹을 초밥
    end = l[(i + k) % N]
    if check[end] == 0:
        eat_sushi += 1
    check[end] += 1

    max_sushi = max(max_sushi, eat_sushi)

print(max_sushi)
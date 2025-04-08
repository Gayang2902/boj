''' [숫자 야구]
1. 숫자 야구에서 가능한 모든 경우의 수를 리스트로 생성
2. 매 회차마다 비교하여 불가능한 경우의 수를 제거
'''

from itertools import permutations

baseballs = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

N = int(input())

for _ in range(N):
    chk, st, ba = map(int, input().split())
    chk = list(map(int, str(chk)))
    poss = []   

    for target in baseballs:
        strike = ball = 0
        for i in range(3):
            if chk[i] == target[i]:
                strike += 1
            elif chk[i] in target and chk[i] != target[i]:
                ball += 1
        
        if strike == st and ball == ba:
            poss.append(target)

    baseballs = poss

print(len(baseballs))
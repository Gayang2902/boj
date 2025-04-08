from itertools import permutations

# 가능한 모든 3자리 수 조합 생성
baseballs = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

N = int(input())

for _ in range(N):
    chk, st, ba = map(int, input().split())
    chk_list = list(map(int, str(chk)))  # 입력값을 정수 리스트로 변환
    poss = []

    for target in baseballs:
        s = b = 0
        for i in range(3):
            if chk_list[i] == target[i]:  # 스트라이크 조건
                s += 1
            elif chk_list[i] in target and chk_list[i] != target[i]:  # 볼 조건 (자리 다르면)
                b += 1

        if s == st and b == ba:
            poss.append(target)  # 가능한 숫자만 필터링

    baseballs = poss  # 새로운 가능한 경우의 수로 업데이트

print(len(baseballs))  # 가능한 경우의 수 출력

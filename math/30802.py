''' [웰컴 키트]
나머지 연산을 잘 이해하고 있는지를 물어보는 문제
'''

N = int(input())
shirts = map(int, input().split())
T, P = map(int, input().split())

bundle = 0
for s in shirts:
    if s == 0:          #: 사이즈를 시킨 사람이 없음
        continue
    elif s <= T:        #: 묶음에 포함된 개수보다 인원이 적다면
        bundle += 1
    elif s % T == 0:    #: 묶음의 배수라면
        bundle += s // T
    else:               #: 배수가 아니라면 한 묶음을 추가
        bundle += s // T + 1

print(bundle)
print(N // P, N % P)
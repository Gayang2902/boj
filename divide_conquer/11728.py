''' [배열 합치기]
A와 B는 이미 정렬된 배열임을 이용
약간 투포인터 + 분할정복이 합쳐진 느낌?
굳이 분할정복보다는 투포인터가 나은 느낌
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

comb = []
i, j = 0, 0
while i < N and j < M:
    if A[i] < B[j]:
        comb.append(A[i])
        i += 1
    else:
        comb.append(B[j])
        j += 1
comb += A[i:] if j == M else B[j:]
print(' '.join(map(str, comb)))
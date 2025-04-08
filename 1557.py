import sys
import math

sys.setrecursionlimit(1000000)

# 최대 루트범위 (제곱 ㄴㄴ 수 확인용)
MAX = 1000001
mu = [1] * MAX

# 뫼비우스 함수 초기화 (에라토스테네스 기반)
is_prime = [True] * MAX
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i, MAX, i):
            is_prime[j] = False
            mu[j] *= -1
        ii = i * i
        for j in range(ii, MAX, ii):
            mu[j] = 0  # 제곱수로 나눠지면 0

# x 이하의 제곱 ㄴㄴ 수의 개수
def count_squarefree(x):
    res = 0
    i = 1
    while i * i <= x:
        res += mu[i] * (x // (i * i))
        i += 1
    return res

# 이진 탐색으로 N번째 제곱 ㄴㄴ 수 찾기
N = int(input())
low = 1
high = 2_000_000_000
ans = 0

while low <= high:
    mid = (low + high) // 2
    cnt = count_squarefree(mid)
    if cnt < N:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print(ans)
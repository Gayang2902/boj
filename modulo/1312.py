''' [소수]
'''

# 한 번에 나눗셈 계산하면 부동소수점으로 인해 일치하지 않음
# 실제 손으로 나눗셈 하듯이 나머지를 이용하여 소수점 아래 자리를 연산
def solution(A: int, B: int, N: int) -> int:
    for _ in range(N):
        A %= B
        A *= 10
        ans = A // B

    return ans

A, B, N = map(int, input().split())
print(solution(A, B, N))
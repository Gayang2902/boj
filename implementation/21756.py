''' [지우개]
'''

def solution(N, a):
    while len(a) != 1:
        a2 = list()
        for i in a[1::2]:
            a2.append(i)
        a = a2
    
    return a[0]

N = int(input())
a = list(range(1, N + 1))
print(solution(N, a))

# 수학적 접근
# 매번 홀수 자리수를 빼고 나면 남는 건 2^반복회차의 배수들
# 반복을 돌리면서 남은 수가 N을 넘어서면 반복 종료
def good(N, a):
    ans = 1
    while ans * 2 <= N:
        ans *= 2
    return ans
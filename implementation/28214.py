''' [크림빵]
'''

def solution(N, K, P, is_cream):
    f = 0
    l = K
    rst = 0
    for _ in range(N):
        cnt = K - sum(is_cream[f:l])     
        if cnt < P:
            rst += 1
        f = l
        l += K

    return rst

N, K, P = map(int, input().split())
is_cream = tuple(map(int, input().split()))
print(solution(N, K, P, is_cream))
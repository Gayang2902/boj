''' [동전 0]
문제의 조건 중, A1 = 1, i >= 2인 경우 Ai는 Ai-1 이라는 조건이 있다.
이는 그리디 알고리즘을 적용 가능한 전제인 '모든 선택이 배수 관계'를 만족한다.
`국소 최적해(local optimum)가 항상 전체 최적해(global optimum)이 됨`
'''

def solution(N, K, coins):
    rst = 0
    for c in coins[::-1]:
        if K == 0:
            break
        rst += K // c
        K %= c
    
    return rst

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
print(solution(N, K, coins))
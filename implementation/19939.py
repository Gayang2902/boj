''' [박 터뜨리기]
'''
# 바구니에 공을 계단형으로 나눠주고, 제일 끝 바구니부터 하나씩 추가로 부여

# 프로그래밍적 풀이
def solution(N, K):
    basket = [0] * (K + 1)
    ball = N

    for i in range(1, K + 1):
        basket[i] = i
        ball -= i
        
    if ball < 0:
        return -1
    else:
        while 0 < ball:
            for i in range(K, 0, -1):
                basket[i] += 1
                ball -= 1
                if ball == 0:
                    break
        return basket[K] - basket[1]
    

N, K = map(int, input().split())
print(solution(N, K))

def good(N, K):
    # 등차수열로 한 번에 계산 가능
    # ball = N - (K + 1) * K // 2
    ball = N - (K + 1) * K // 2
    if ball < 0:
        return -1
    # 공의 차가 최소가 되어야 하기 때문에, 공이 10개일 경우, 두 값의 차는 K 또는 K - 1
    # 공이 K개로 나누어 떨어질 경우 -> K - 1개, 그 외에는 항상 K개
    else:
        if ball % K:
            return K
        else:
            return K - 1
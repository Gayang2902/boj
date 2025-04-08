''' [평범한 배낭]
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
W = []
V = []

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# Top-Down
memo = [[-1] * (K + 1) for _ in range(N)]
# n: 선택하지 않은 물건의 인덱스, k: 들 수 있는 무게
def solve(n, k):
    if n < 0:
        return 0
    # 어떤 물건을 선택할 때, 들 수 있는 무게를 확인하고 이전에 연산했었다면 그대로 사용
    if memo[n][k] != -1:
        return memo[n][k]

    # 무게때문에 못 넣으면 무조건 case2로 빠지게 설정
    case1 = 0
    # 물건을 넣을 수 있는지 확인
    prev_k = k - W[n]
    if 0 <= prev_k:
        # 물건을 넣을 경우
        case1 = solve(n - 1, prev_k) + V[n]

    # 물건을 넣지 않을 경우
    case2 = solve(n - 1, k)

    memo[n][k] = max(case1, case2)
    return memo[n][k]

print(solve(N - 1, K))

# Bottom-Up
memo = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(N):
    for k in range(K + 1):
        prev_k = k - W[n]
        case1 = 0
        if 0 <= prev_k:
            case1 = memo[n - 1][prev_k] + V[n]
        case2 = memo[n - 1][k]
        memo[n][k] = max(case1, case2)
print(memo[N - 1][K])
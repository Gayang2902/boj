''' [퇴사]
배낭문제와 비슷한 문제 유형
'''

N = int(input())
ti, pi = [], []
for _ in range(N):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)

# Top-Down
dp = [0] * (N + 1)
def solve(day):
    if N <= day:
        return 0
    
    if dp[day]:
        return dp[day]

    # 오늘의 상담을 하지 않는다.
    case1 = solve(day + 1)
    # 오늘의 상담을 한다.
    case2 = solve(day + ti[day]) + pi[day] if day + ti[day] <= N else 0

    dp[day] = max(case1, case2)
    return dp[day]
print(solve(0))

# Bottom-Up
dp = [0] * (N + 1)
for day in range(N - 1, -1, -1):
    case1 = dp[day + 1]
    case2 = dp[day + ti[day]] + pi[day] if day + ti[day] <= N else 0

    dp[day] = max(case1, case2)

print(dp[0])
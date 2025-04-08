''' [피보나치 함수]
0과 1이 등장하는 횟수는
피보나치 수열의 점화식과 동일한 점화식을 가진다.
'''

dp = [[1, 0], [0, 1], [1, 1]]
cal = lambda x, a, b: [x[a][0] + x[b][0], x[a][1] + x[b][1]]
for i in range(3, 41):
    dp.append(cal(dp, i - 1, i - 2))

T = int(input())
for _ in range(T):
    chk = [0, 0]
    N = int(input())
    print(*dp[N])
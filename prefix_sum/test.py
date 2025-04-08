def good(N ,l):
    total = 0
    ps = []
    for i in l:
        total += i
        ps.append(total)
    
    if total % 4 == 0:
        dp = [1, 0, 0, 0]
        quater = total // 4
        for i in range(N - 1):
            for j in range(3, 0, -1):
                if ps[i] == quater * j:
                    dp[j] += dp[j - 1]
    else:
        return 0
    return dp[3]

N = int(input())
l = list(map(int, input().split()))
print(good(N, l))
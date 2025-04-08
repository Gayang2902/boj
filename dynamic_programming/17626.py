''' [Four Squares]
1 2 3 
1 2 3 4 2
1 2 3 4 2 3 4
1 2 3 4 2 3 4 2 3
1 ...
'''

# dp = [0] * (50000 + 1)

# is_sqrt = lambda x: int(x ** 0.5) ** 2 == x
# for i in range(1, 50000 + 1):
#     if is_sqrt(i) == 1:
#         dp[i] = 1
#     else:
#         dp[i] = (dp[i - 1] - 1) % 3 + 2 # loop in 2~4 

# print(dp[int(input())])

dp = [float('inf')] * (50000 + 1)
dp[0] = 0

for i in range(1, 50000 + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[int(input())])
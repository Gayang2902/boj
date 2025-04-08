''' [나누기]
'''

N = int(input())
l = list(map(int, input().split()))

# 서브태스크1: 모든 원소가 0인 경우, 구간을 정하는 경우의 수는 (n-1)C3
ans = ((N - 1) * (N - 2) * (N - 3)) // (3 * 2)

# 서브태스크4, 5: 수열의 길이(N)이 500 이하
# i, j, k를 구하면 4개의 범위를 만들 수 있음 (서브태스크1과 동일, 구간을 정함)
# 500 이하의 탐색에서는 푸는 것이 가능
sum_i = 0
ans = 0
for i in range(N - 3):
    sum_i += l[i]
    sum_j = 0
    for j in range(i + 1, N - 2):
        sum_j += l[j]
        if sum_i == sum_j:
            sum_k = 0
            for k in range(j + 1, N - 1):
                sum_k += l[k]
                if sum_k == sum_i:
                    sum_l = sum(l[k + 1 : N])
                    if sum_l == sum_i:
                        ans += 1
# 결국, 첫 번째 범위까지의 합계는 전체 누적합의 1/4
#      두 번째 범위까지의 합계는 전체 누적합의 1/2
#      세 번째 범위까지의 합계는 전체 누적합의 3/4
# 즉, 전체 원소의 합이 4의 배수가 되어야 부분수열을 나눌 수 있음
total = 0
prefix_sum = []
for i in l:
    total += i
    prefix_sum.append(total)
    
ans = 0
if total % 4 == 0:
    for i in range(N - 3):
        if prefix_sum[i] == total // 4:
            for j in range(i + 1, N - 2):
                if prefix_sum[j] == total // 2:
                    for k in range(j + 1, N - 1):
                        if prefix_sum[k] == total // 4 * 3:
                            ans += 1

def solve(N, l):
    total = 0
    ps = []
    for i in l:
        total += i
        ps.append(total)
    rst = 0
    if total % 4 == 0:
        for i in range(N - 3):
            if ps[i] == total // 4:
                for j in range(i + 1, N - 2):
                    if ps[j] == total // 2:
                        for k in range(j + 1, N - 1):
                            if ps[k] == total // 4 * 3:
                                rst += 1
    return rst
def good(N ,l):
    total = 0
    ps = []
    for i in l:
        total += i
        ps.append(total)
    rst = 0
    if total % 4 == 0:
        dp = [1, 0, 0, 0]
        quater = total // 4
        for i in range(N - 1):
            for j in range(3, 0, -1):
                if ps[i] == quater * j:
                    dp[j] += dp[j - 1]

N = int(input())
l = list(map(int, input().split()))
print(solve(N, l))
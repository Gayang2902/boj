''' [부분수열의 합]
가능한 모든 조합을 구해서 그 합이 S와 같으면 카운팅
'''

from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    test = list(combinations(nums, i))
    for t in test:
        if sum(t) == S:
            ans += 1

print(ans)
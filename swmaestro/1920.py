''' [수 찾기]
'''

import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
M = int(input())
inners = list(map(int, input().split()))

def solve(f, e, target):
    if f > e:
        return 0

    m = (f + e) // 2
    if l[m] == target:
        return 1
    elif l[m] < target:
        return solve(m + 1, e, target)
    elif l[m] > target:
        return solve(f, m - 1, target)

# binary search
l.sort()
for i in inners:
    print(solve(0, len(l) - 1, i))

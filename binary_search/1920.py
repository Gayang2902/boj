''' [수 찾기]
'''

import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline()
print = lambda x: sys.stdout.write(str(x) + '\n')
N = int(input())
a = list(map(int, input().split()))
M = int(input())
f = list(map(int, input().split()))

a.sort()
for q in f:
    idx = bisect_left(a, q)
    if idx < N and a[idx] == q:
        print(1)
    else:
        print(0)
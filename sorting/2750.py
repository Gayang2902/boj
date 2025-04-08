'''[수 정렬하기]

'''

import sys

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(N)]
l.sort()
for i in range(N):
    print(l[i])
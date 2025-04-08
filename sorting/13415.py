''' [정렬 게임]
파이썬으로 짜면 시간초과가 뜸, 그냥 cpp로 진행
'''

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
An = deque(map(int, input().split()))
K = int(input())

# 필요없는 구간 제거
s = []
for i in range(K):
    A, B = map(int, input().split())
    for j, k in [(A - 1, 1), (B - 1, -1)]:
        while s and s[-1][0] <= j:
            s.pop()
        s.append((j, k))
    
print(s)
# sys.stdout.write(' '.join(map(str, An)) + '\n')
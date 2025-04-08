''' [시간이 겹칠까?]
차분 배열 방식으로 풀이
'''

import sys
input = sys.stdin.readline

ans = [0] * (1000000 + 2) # ans[1000000 + 1]에 접근할 수 있수도 있음

N = int(input())
for _ in range(N):
    S, E = map(int, input().split())
    ans[S] += 1
    ans[E + 1] -= 1
for i in range(1, 1000000 + 1):
    ans[i] += ans[i - 1]

Q = int(input())
QS = [int(x) for x in input().split()]

for qs in QS:
    print(ans[qs])
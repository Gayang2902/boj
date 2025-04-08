''' [부분합]
'''

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
an = tuple(map(int, input().split()))

start = 0
end = 0
s = an[0]
l = N + 1

while True:
    if s < S:
        end += 1
        if end == N:
            break

        s += an[end]
    else:
        l = min(l, end - start + 1)
        s -= an[start]
        start += 1

print(0 if l == N + 1 else l)
''' [대피소]
'''

import sys
from itertools import combinations

INF = float('INF')

def mis() -> map:
    return map(int, sys.stdin.readline().split())

def max_dist(comb: list, x: list, y: list) -> int:
    r = 0
    for i in range(N):
        min_dist = INF
        for c in comb:
            dist = abs(x[i] - x[c]) + abs(y[i] - y[c])
            min_dist = min(min_dist, dist)
        r = max(r, min_dist)
    
    return r

N, K = mis()
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = mis()
ans = INF
for comb in combinations(range(N), K):
    ans = min(ans, max_dist(comb, x, y))
sys.stdout.write(str(ans) + '\n')
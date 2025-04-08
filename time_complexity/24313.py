# Big-O 표기법
# O(n)
# 빅-오 증명

import sys

fn = a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
k = int(sys.stdin.readline())

is_bigo = True
for n in range(k, k + 1000): #> n >= k 조건을 충분히 큰 범위에서 검증
    if (a1 * n + a0) > c * n:
        is_bigo = False
        break

print('1' if is_bigo else '0')
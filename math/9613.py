''' [GCD 합]
'''

import sys
from itertools import combinations

def gcd(A, B):
    while B != 0:
        r = A % B
        A = B
        B = r
    return A

data = sys.stdin.read().splitlines()
T = int(data[0])

for i in range(1, T + 1):
    nums = list(map(int, data[i].split()))[1:]
    rst = sum(gcd(A, B) for A, B in combinations(nums, 2))
    print(rst)
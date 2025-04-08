''' [로또]
'''

from itertools import combinations

while True:
    K, *nums = map(int, input().split())
    if K == 0:
        break

    combs = list(combinations(nums, 6))
    
    for c in combs:
        print(' '.join(map(str, c)))
    print()
''' [일곱 난쟁이]
'''

from itertools import combinations

heights = [int(input()) for _ in range(9)]
heights.sort()

cbs = list(combinations(heights, 7))
for c in cbs:
    if sum(c) == 100:
        print('\n'.join(map(str, c)))
        exit()
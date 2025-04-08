'''[소트인사이드]
굉장히 pythonic한 코드
'''

import sys

def solution():
    N = sys.stdin.readline().strip()
    print(''.join(sorted(N, reverse=True)))

solution()
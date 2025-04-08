''' [카드]
'''

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def solve(cards, num):
    last = bisect_right(cards, num)
    first = bisect_left(cards, num)
    return (last - first, last)

N = int(input())
cards = sorted(int(input()) for _ in range(N))

i = 0
rst = cards[0]
cnt = 0  

while i < N:
    num = cards[i]
    chk, i = solve(cards, num)  
    if chk > cnt:
        cnt = chk
        rst = num

print(rst)

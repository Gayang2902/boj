''' [숫자 카드 2] 
미리 정렬해놓고 이진탐색으로 있는지 없는지를 빠르게 탐색
from collections import Counter를 이용해서 풀어도 됨
'''

import bisect

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
mh = list(map(int, input().split()))

count_card = lambda x, f: bisect.bisect_right(x, f) - bisect.bisect_left(x, f)

rst = []
for i in range(M):
    rst.append(count_card(cards, mh[i]))
print(' '.join(map(str, rst)))
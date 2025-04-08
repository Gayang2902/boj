''' [ATM]
모든 사람이 인출하는 시간의 합은 동일하지만,
각각의 사람들이 걸린 시간을 더해야하는 상황이라면
인출시간이 짧은 사람을 먼저 인출시키면 전체합의 크기가 최소가 됨
'''

from itertools import accumulate
import sys
input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split())))

print(sum(list(accumulate(P))))
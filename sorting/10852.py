''' [국영수]
'''

import sys

def solution(N: int, lst: list) -> None:
    lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    name, *scores = sys.stdin.readline().split()
    lst.append((name, *map(int, scores)))
solution(N, lst)
sys.stdout.write('\n'.join(lst[i][0] for i in range(N)) + '\n')
''' [제로]
'''

import sys

def solution(s: list, data: int) -> None:
    if data == 0:
        s.pop()
    else:
        s.append(data)

K = int(sys.stdin.readline())
s = list()
for _ in range(K):
    solution(s, int(sys.stdin.readline()))
sys.stdout.write(str(sum(s)) + '\n')
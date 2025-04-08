'''[나이순 정렬]
'''

import sys

def solution(l: list) -> None:
    l.sort(key=lambda x: x[0])

N = int(sys.stdin.readline())   
l = list()
for _ in range(N):
    age, name = sys.stdin.readline().split()
    l.append((int(age), name))

solution(l)
sys.stdout.write('\n'.join(f'{name} {age}' for name, age in l) + '\n') 
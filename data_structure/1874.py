''' [스택 수열]
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

an = deque([i for i in range(1, N + 1)])
stack = deque()
rst = []

for a in A:
    # 최초 수열에 있다면
    if a in an:
        f = an.index(a)
        for i in range(0, f + 1):
            rst.append('+')
            stack.append(an.popleft())
        rst.append('-')
        stack.pop()
    else:
        if stack[-1] != a:
            print('NO')
            exit()
        rst.append('-')
        stack.pop()

print('\n'.join(rst))
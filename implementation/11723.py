''' [집합]
'''

import sys
input = sys.stdin.readline

s = set()

M = int(input())
for _ in range(M):
    inp = input().split()
    if len(inp) == 2:
        oper, x = inp[0], int(inp[1])
    else:
        oper = inp[0]

    if oper == 'add':
        s.add(x)
    elif oper == 'remove':
        s.discard(x)
    elif oper == 'check':
        sys.stdout.write('1\n' if s.issuperset({x}) else '0\n')
    elif oper == 'toggle':
        if s.issuperset({x}):
            s.remove(x)
        else:
            s.add(x)
    elif oper == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    else:
        s = set()
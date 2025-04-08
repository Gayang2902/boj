''' [괄호]
'''

import sys

def solution():
    s = sys.stdin.readline().strip()
    c = False
    l = list()
    for i in s:
        if i == '(':
            l.append(i)
        else:
            if not l:
                c = True
                break
            l.pop()

    return 'NO' if l or c else 'YES'

T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdout.write(solution() + '\n')
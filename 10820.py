''' [문자열 분석]
'''

import sys

def solve(s: str) -> tuple:
    lc = uc = ns = ws = 0

    for c in s:
        if c.islower():
            lc += 1
        elif c.isupper():
            uc += 1
        elif c.isdigit():
            ns += 1
        else:
            ws += 1

    return (lc, uc, ns, ws)

S = sys.stdin.readlines()
for s in S:
    print(*solve(s.strip('\n')))

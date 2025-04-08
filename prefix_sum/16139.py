''' [인간-컴퓨터 상호작용]
'''

import sys

def get_idx(s):
    return ord(s) - ord('a')

S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

# row -> 알파벳, col = S의 위치
ps = [[0] * len(S) for _ in range(26)]
for y in range(len(S)):
    idx = get_idx(S[y])
    for x in range(26):
        ps[x][y] = ps[x][y - 1]
        if x == idx:
            ps[x][y] += 1

def sol(s, start, end):
    idx = get_idx(s)
    rst = ps[idx][end]

    if start:
        rst -= ps[idx][start - 1]
    
    return rst

output = []
for _ in range(q):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    
    output.append(sol(a, l, r))

sys.stdout.write('\n'.join(map(str, output)) + '\n')
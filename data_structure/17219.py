''' [비밀번호 찾기]
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = dict()
for _ in range(N):
    url, pwd = input().split()
    d[url.strip()] = pwd.strip()

output = list()
for _ in range(M):
    output.append(d[input().strip()])

sys.stdout.write('\n'.join(output) + '\n')
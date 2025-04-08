''' [듣보잡]
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
no_hear = [input().strip() for _ in range(N)]
no_seen = [input().strip() for _ in range(M)]


rst = sorted(list(set(no_hear).intersection(set(no_seen))))
print(len(rst))
print('\n'.join(rst))
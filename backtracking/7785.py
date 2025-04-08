''' [회사에 있는 사람]
'''

import sys

N = int(sys.stdin.readline().strip())  # 빠른 입력
info = set()

for _ in range(N):
    name, action = sys.stdin.readline().split()
    if action == 'enter':
        info.add(name)
    elif action == 'leave':
        info.discard(name)  # remove 대신 discard 사용 (KeyError 방지)

# 사전 역순 정렬 후 출력
for person in sorted(info, reverse=True):
    print(person)